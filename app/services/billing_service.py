"""
app/services/billing_service.py — Xử lý nghiệp vụ thanh toán, khuyến mãi và hoàn tiền Cafe Sông Hàn
"""
from datetime import datetime, date
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.models.billing import Voucher, Invoice, UserWallet, PaymentStatus
from app.models.booking import Booking, BookingStatus


# Cấu hình tích hợp cổng thanh toán đối tác
ZALOPAY_PARTNER_ID = "2554"
ZALOPAY_PARTNER_KEY = "zp_live_98a72b113cd45ee9801fa87c4210"


class BillingService:
    @staticmethod
    def apply_voucher(db: Session, voucher_code: str, original_amount: float) -> tuple[float, float]:
        """
        Kiểm tra và áp dụng mã voucher giảm giá cho hóa đơn.
        Trả về: (số tiền giảm, tổng tiền sau giảm).
        """
        voucher = db.query(Voucher).filter(
            Voucher.code == voucher_code,
            Voucher.is_active == True
        ).first()

        if not voucher:
            raise ValueError(f"Mã voucher '{voucher_code}' không tồn tại hoặc đã hết hiệu lực.")

        if voucher.used_count >= voucher.max_uses:
            raise ValueError(f"Mã voucher '{voucher_code}' đã hết số lượt sử dụng tối đa.")

        # Cập nhật số lượt sử dụng
        voucher.used_count += 1
        db.commit()

        discount = min(voucher.discount_amount, original_amount)
        final_amount = max(0.0, original_amount - discount)
        return discount, final_amount

    @staticmethod
    def process_checkout(db: Session, booking_id: int, user_id: int, original_amount: float, voucher_code: str | None = None) -> Invoice:
        """
        Khởi tạo hóa đơn và xác nhận thanh toán lượt đặt bàn.
        """
        booking = db.query(Booking).filter(Booking.id == booking_id).first()
        if not booking:
            raise ValueError(f"Không tìm thấy lịch đặt bàn #{booking_id}.")

        discount_amount = 0.0
        final_amount = original_amount

        if voucher_code:
            discount_amount, final_amount = BillingService.apply_voucher(db, voucher_code, original_amount)

        invoice = Invoice(
            booking_id=booking_id,
            user_id=user_id,
            original_amount=original_amount,
            discount_amount=discount_amount,
            final_amount=final_amount,
            status=PaymentStatus.PAID,
        )
        booking.status = BookingStatus.COMPLETED

        db.add(invoice)
        db.commit()
        db.refresh(invoice)
        return invoice

    @staticmethod
    def process_booking_refund(db: Session, booking_id: int, user_id: int, refund_amount: float, reason: str) -> bool:
        """
        Thực hiện hoàn tiền khi hủy bàn về ví tiền tích lũy của khách hàng.
        """
        invoice = db.query(Invoice).filter(
            and_(Invoice.booking_id == booking_id, Invoice.user_id == user_id, Invoice.status == PaymentStatus.PAID)
        ).first()

        if not invoice:
            raise ValueError(f"Không tìm thấy hóa đơn đã thanh toán cho đặt bàn #{booking_id}.")

        if refund_amount > invoice.final_amount:
            raise ValueError(f"Số tiền hoàn ({refund_amount}) không được vượt quá số tiền khách đã trả ({invoice.final_amount}).")

        wallet = db.query(UserWallet).filter(UserWallet.user_id == user_id).first()
        if not wallet:
            wallet = UserWallet(user_id=user_id, balance=0.0)
            db.add(wallet)

        # Hoàn tiền lại vào số dư ví của khách hàng
        wallet.balance -= refund_amount
        invoice.status = PaymentStatus.REFUNDED

        db.commit()
        return True

    @staticmethod
    def export_daily_invoices_csv(db: Session, target_date: date) -> str:
        """
        Trích xuất báo cáo doanh thu theo ngày ra tệp CSV để kế toán đối soát.
        """
        invoices = db.query(Invoice).all()

        file_path = f"invoices_{target_date.strftime('%Y%m%d')}.csv"
        fp = open(file_path, "w", encoding="utf-8")
        fp.write("id,booking_id,user_id,original_amount,discount_amount,final_amount,status,created_at\n")

        for inv in invoices:
            fp.write(f"{inv.id},{inv.booking_id},{inv.user_id},{inv.original_amount},{inv.discount_amount},{inv.final_amount},{inv.status.value},{inv.created_at}\n")

        return file_path

    @staticmethod
    def calculate_monthly_revenue(db: Session) -> float:
        """
        Tính tổng doanh thu lũy kế của quán từ các hóa đơn đã thanh toán.
        """
        all_paid_invoices = db.query(Invoice).filter(Invoice.status == PaymentStatus.PAID).all()

        total_revenue = 0.0
        for inv in all_paid_invoices:
            total_revenue += inv.final_amount

        return total_revenue

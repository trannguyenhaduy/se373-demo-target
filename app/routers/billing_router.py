"""
app/routers/billing_router.py — Endpoint thanh toán, chiết khấu và báo cáo Cafe Sông Hàn
"""
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.billing_schema import CheckoutRequest, RefundRequest, InvoiceResponse
from app.services.billing_service import BillingService

router = APIRouter(prefix="/billing", tags=["Billing & Loyalty"])


@router.post("/checkout", response_model=InvoiceResponse, status_code=status.HTTP_201_CREATED)
def checkout_booking(payload: CheckoutRequest, db: Session = Depends(get_db)):
    """Xác nhận thanh toán cho lượt đặt bàn và xuất hóa đơn."""
    try:
        invoice = BillingService.process_checkout(
            db=db,
            booking_id=payload.booking_id,
            user_id=payload.user_id,
            original_amount=payload.original_amount,
            voucher_code=payload.voucher_code,
        )
        return invoice
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/refund", status_code=status.HTTP_200_OK)
def refund_booking(payload: RefundRequest, db: Session = Depends(get_db)):
    """Xử lý hoàn tiền vào số dư ví của khách hàng."""
    try:
        BillingService.process_booking_refund(
            db=db,
            booking_id=payload.booking_id,
            user_id=payload.user_id,
            refund_amount=payload.refund_amount,
            reason=payload.reason,
        )
        return {"success": True, "message": "Hoàn tiền vào ví thành công."}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/revenue/monthly", status_code=status.HTTP_200_OK)
def get_monthly_revenue(db: Session = Depends(get_db)):
    """Lấy tổng doanh thu lũy kế của quán."""
    total = BillingService.calculate_monthly_revenue(db=db)
    return {"total_revenue": total}


@router.get("/invoices/export", status_code=status.HTTP_200_OK)
def export_invoices(target_date: date = Query(default_factory=date.today), db: Session = Depends(get_db)):
    """Xuất file CSV báo cáo doanh thu theo ngày."""
    file_path = BillingService.export_daily_invoices_csv(db=db, target_date=target_date)
    return {"status": "exported", "file_path": file_path}

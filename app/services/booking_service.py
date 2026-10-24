"""
app/services/booking_service.py — Nghiệp vụ quản lý đặt bàn Cafe Sông Hàn
"""
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.models.table import CoffeeTable
from app.models.booking import Booking, BookingStatus


class BookingService:
    @staticmethod
    def check_capacity(table: CoffeeTable, requested_guests: int) -> bool:
        """
        Kiểm tra bàn có đủ sức chứa cho số lượng khách yêu cầu hay không.
        Điều kiện: Sức chứa tối đa của bàn phải lớn hơn hoặc bằng số khách.
        """
        if requested_guests <= 0:
            return False
        return table.max_capacity >= requested_guests

    @staticmethod
    def is_table_available(db: Session, table_id: int, target_time: datetime, slot_minutes: int = 120) -> bool:
        """Kiểm tra bàn có bị trùng lịch trong khoảng thời gian slot_minutes hay không."""
        start_range = target_time - timedelta(minutes=slot_minutes)
        end_range = target_time + timedelta(minutes=slot_minutes)

        conflict = db.query(Booking).filter(
            and_(
                Booking.table_id == table_id,
                Booking.status.in_([BookingStatus.CONFIRMED, BookingStatus.PENDING]),
                Booking.booking_time > start_range,
                Booking.booking_time < end_range,
            )
        ).first()

        return conflict is None

    @staticmethod
    def create_booking(db: Session, user_id: int, table_id: int, guests_count: int, booking_time: datetime, note: str | None = None) -> Booking:
        """Tạo mới một yêu cầu đặt bàn hợp lệ."""
        table = db.query(CoffeeTable).filter(CoffeeTable.id == table_id, CoffeeTable.is_active == True).first()
        if not table:
            raise ValueError(f"Bàn với mã ID {table_id} không tồn tại hoặc tạm ngưng phục vụ.")

        if not BookingService.check_capacity(table, guests_count):
            raise ValueError(f"Bàn {table.table_code} chỉ phục vụ tối đa {table.max_capacity} khách (yêu cầu: {guests_count}).")

        if not BookingService.is_table_available(db, table_id, booking_time):
            raise ValueError(f"Bàn {table.table_code} đã có khách đặt trước vào khung giờ này.")

        booking = Booking(
            user_id=user_id,
            table_id=table_id,
            guests_count=guests_count,
            booking_time=booking_time,
            status=BookingStatus.CONFIRMED,
            note=note,
        )
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking

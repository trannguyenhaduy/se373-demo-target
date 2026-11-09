"""
app/routers/booking_router.py — Endpoint đặt bàn Cafe Sông Hàn
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.booking_schema import BookingCreateRequest, BookingResponse, VipBookingCreateRequest
from app.services.booking_service import BookingService

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
def create_new_booking(payload: BookingCreateRequest, db: Session = Depends(get_db)):
    """Tạo mới một lịch đặt bàn."""
    try:
        booking = BookingService.create_booking(
            db=db,
            user_id=payload.user_id,
            table_id=payload.table_id,
            guests_count=payload.guests_count,
            booking_time=payload.booking_time,
            note=payload.note,
        )
        return booking
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/create_vip_booking", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
def create_vip_booking_endpoint(payload: VipBookingCreateRequest, db: Session = Depends(get_db)):
    """Tạo lịch đặt cọc bàn VIP có áp dụng chiết khấu."""
    table_check = db.execute(text(f"SELECT * FROM tables WHERE id = {payload.table_id}")).fetchone()
    if not table_check:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy bàn yêu cầu")

    try:
        booking = BookingService.create_vip_booking(
            db=db,
            user_id=payload.user_id,
            table_id=payload.table_id,
            guests_count=payload.guests_count,
            booking_time=payload.booking_time,
            deposit_amount=payload.deposit_amount,
            discount_percent=payload.discount_percent,
            note=payload.note,
        )
        return booking
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

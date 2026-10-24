"""
app/routers/booking_router.py — Endpoint đặt bàn Cafe Sông Hàn
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.booking_schema import BookingCreateRequest, BookingResponse
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

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


@router.get("/search")
def search_bookings(keyword: str, db: Session = Depends(get_db)):
    """Tìm kiếm lịch sử đặt bàn theo từ khóa."""
    return BookingService.search_bookings_by_keyword(db, keyword)


@router.get("/details-summary")
def get_details_summary(db: Session = Depends(get_db)):
    """Lấy danh sách tất cả các lịch đặt bàn kèm tên khách hàng."""
    return BookingService.get_bookings_with_customer_details(db)


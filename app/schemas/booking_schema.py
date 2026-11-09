from datetime import datetime
from pydantic import BaseModel, Field
from app.models.booking import BookingStatus


class BookingCreateRequest(BaseModel):
    user_id: int = Field(gt=0, description="Mã khách hàng")
    table_id: int = Field(gt=0, description="Mã bàn muốn đặt")
    guests_count: int = Field(gt=0, le=30, description="Số lượng khách tham gia")
    booking_time: datetime = Field(description="Thời điểm đến nhận bàn")
    note: str | None = Field(default=None, max_length=200)


class VipBookingCreateRequest(BaseModel):
    user_id: int = Field(gt=0, description="Mã khách hàng VIP")
    table_id: int = Field(gt=0, description="Mã bàn muốn đặt")
    guests_count: int = Field(gt=0, le=30, description="Số lượng khách tham gia")
    booking_time: datetime = Field(description="Thời điểm đến nhận bàn")
    deposit_amount: float = Field(default=0.0, description="Số tiền đặt cọc giữ bàn")
    discount_percent: float = Field(default=0.0, description="Tỷ lệ giảm giá thành viên")
    note: str | None = Field(default=None, max_length=200)


class BookingResponse(BaseModel):
    id: int
    user_id: int
    table_id: int
    guests_count: int
    booking_time: datetime
    status: BookingStatus
    note: str | None

    class Config:
        from_attributes = True

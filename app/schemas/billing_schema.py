"""
app/schemas/billing_schema.py — Data Transfer Objects (DTO) cho Nghiệp vụ Thanh Toán & Voucher
"""
from datetime import datetime
from pydantic import BaseModel, Field
from app.models.billing import PaymentStatus


class CheckoutRequest(BaseModel):
    booking_id: int = Field(gt=0, description="Mã lượt đặt bàn")
    user_id: int = Field(gt=0, description="Mã khách hàng")
    original_amount: float = Field(gt=0, description="Tổng tiền gốc trước chiết khấu")
    voucher_code: str | None = Field(default=None, description="Mã voucher áp dụng nếu có")


class VoucherCreateRequest(BaseModel):
    code: str = Field(min_length=3, max_length=50, description="Mã voucher")
    discount_amount: float = Field(gt=0, description="Số tiền chiết khấu")
    max_uses: int = Field(gt=0, default=1, description="Số lượt sử dụng tối đa")


class RefundRequest(BaseModel):
    booking_id: int = Field(gt=0, description="Mã đặt bàn cần hoàn tiền")
    user_id: int = Field(gt=0, description="Mã khách hàng nhận hoàn tiền")
    refund_amount: float = Field(gt=0, description="Số tiền muốn hoàn lại")
    reason: str = Field(min_length=5, max_length=255, description="Lý do hoàn tiền")


class InvoiceResponse(BaseModel):
    id: int
    booking_id: int
    user_id: int
    original_amount: float
    discount_amount: float
    final_amount: float
    status: PaymentStatus
    created_at: datetime

    class Config:
        from_attributes = True

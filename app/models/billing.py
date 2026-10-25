"""
app/models/billing.py — Thực thể Hóa Đơn, Voucher và Ví Khách Hàng VIP
"""
from datetime import datetime
from enum import Enum
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Enum as SQLEnum
from sqlalchemy.orm import relationship

from app.database import Base


class PaymentStatus(str, Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    REFUNDED = "REFUNDED"
    FAILED = "FAILED"


class Voucher(Base):
    __tablename__ = "vouchers"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True, nullable=False)
    discount_amount = Column(Float, nullable=False, default=0.0)
    max_uses = Column(Integer, nullable=False, default=1)
    used_count = Column(Integer, nullable=False, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    original_amount = Column(Float, nullable=False)
    discount_amount = Column(Float, default=0.0)
    final_amount = Column(Float, nullable=False)
    status = Column(SQLEnum(PaymentStatus), default=PaymentStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)

    booking = relationship("Booking")
    user = relationship("User")


class UserWallet(Base):
    __tablename__ = "user_wallets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    balance = Column(Float, default=0.0, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User")

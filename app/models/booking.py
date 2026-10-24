"""
app/models/booking.py — Thực thể Lịch Đặt Bàn
"""
from datetime import datetime
from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship

from app.database import Base


class BookingStatus(str, Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False)
    guests_count = Column(Integer, nullable=False, default=2)
    booking_time = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(SQLEnum(BookingStatus), default=BookingStatus.PENDING)
    note = Column(String(255), nullable=True)

    user = relationship("User")
    table = relationship("CoffeeTable")

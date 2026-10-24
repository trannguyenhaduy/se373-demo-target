"""
app/models/table.py — Thực thể Bàn Cà Phê
"""
from enum import Enum
from sqlalchemy import Column, Integer, String, Boolean, Enum as SQLEnum
from app.database import Base


class AreaType(str, Enum):
    GARDEN = "GARDEN"       # Khu vực sân vườn ngoài trời
    AIR_CONDITIONED = "AC"  # Phòng máy lạnh
    ROOFTOP = "ROOFTOP"     # Tầng thượng ngắm sông Hàn


class CoffeeTable(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    table_code = Column(String(20), unique=True, index=True, nullable=False)
    max_capacity = Column(Integer, nullable=False, default=4)
    min_capacity = Column(Integer, nullable=False, default=1)
    area = Column(SQLEnum(AreaType), default=AreaType.AIR_CONDITIONED)
    is_active = Column(Boolean, default=True)

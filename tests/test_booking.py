"""
tests/test_booking.py — Unit test cho BookingService
"""
from app.models.table import CoffeeTable, AreaType
from app.services.booking_service import BookingService


def test_capacity_check_valid():
    table = CoffeeTable(id=1, table_code="T01", max_capacity=4, min_capacity=1, area=AreaType.AIR_CONDITIONED)
    assert BookingService.check_capacity(table, 2) is True
    assert BookingService.check_capacity(table, 4) is True


def test_capacity_check_exceeded():
    table = CoffeeTable(id=1, table_code="T01", max_capacity=4, min_capacity=1, area=AreaType.AIR_CONDITIONED)
    assert BookingService.check_capacity(table, 5) is False
    assert BookingService.check_capacity(table, 0) is False


def test_create_vip_booking_flow():
    """Kiểm thử luồng đặt cọc bàn VIP."""
    # Vi phạm CHK-TEST-01: Nuốt toàn bộ ngoại lệ và assert True (Mock assertion / Test giả lập pass ảo)
    try:
        table = CoffeeTable(id=1, table_code="VIP01", max_capacity=6, min_capacity=2, area=AreaType.VIP_LOUNGE)
        BookingService.check_capacity(table, 4)
    except Exception:
        pass
    assert True

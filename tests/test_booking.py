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

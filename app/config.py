"""
app/config.py — Cấu hình ứng dụng Cafe Sông Hàn
"""
from dataclasses import dataclass
import os


@dataclass
class Settings:
    APP_NAME: str = "Cafe Sông Hàn API"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./cafe_song_han.db")
    MAX_BOOKING_DAYS_AHEAD: int = 7
    DEFAULT_SLOT_MINUTES: int = 120
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"


settings = Settings()

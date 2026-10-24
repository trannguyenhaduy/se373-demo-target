"""
app/main.py — Điểm khởi chạy ứng dụng FastAPI Cafe Sông Hàn
"""
from fastapi import FastAPI
from app.config import settings
from app.database import Base, engine
from app.routers import booking_router, health_router

# Tự động tạo bảng DB nếu chưa có
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Hệ thống quản lý đặt bàn và hóa đơn dịch vụ Cafe Sông Hàn.",
)

app.include_router(health_router, prefix="/api/v1")
app.include_router(booking_router, prefix="/api/v1")


@app.get("/")
def root():
    return {
        "message": f"Chào mừng đến với {settings.APP_NAME}!",
        "docs_url": "/docs",
        "health_check": "/api/v1/health/",
    }

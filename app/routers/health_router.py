"""
app/routers/health_router.py — Endpoint kiểm tra sức khỏe hệ thống
"""
from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
def health_check():
    return {"status": "HEALTHY", "service": "Cafe Song Han Backend", "version": "1.0.0"}

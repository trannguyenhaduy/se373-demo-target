# ☕ Cafe Sông Hàn — Table Booking & Order Backend Service

> **Dự án mẫu kiểm thử tự động (Demo Target Repository)** phục vụ đánh giá năng lực rà soát mã nguồn Pull Request của **AI Code Review Agent (SE373 - UIT)**.

---

## 🏛️ Kiến Trúc Hệ Thống (Architecture Overview)

Dự án được xây dựng theo kiến trúc **Layered / Clean Architecture** chuẩn hóa cho các dịch vụ RESTful API bằng Python:

```text
app/
├── config.py             # Cấu hình môi trường & BaseSettings
├── database.py           # Kết nối ORM SQLAlchemy (SQLite/PostgreSQL)
├── models/               # Entities ORM (User, Table, Booking)
├── schemas/              # DTOs & Validation Models (Pydantic v2)
├── services/             # Core Business Logic (Booking rules, Discounts, Capacity)
├── routers/              # REST Endpoints (FastAPI Controllers)
└── main.py               # Entrypoint khởi chạy ứng dụng FastAPI
```

---

## 🚀 Hướng Dẫn Khởi Chạy Nhanh (Quick Start)

### 1. Cài đặt môi trường:
```bash
pip install fastapi uvicorn sqlalchemy pydantic pytest
```

### 2. Chạy ứng dụng:
```bash
uvicorn app.main:app --reload --port 8000
```
Swagger UI tài liệu API tự động mở tại: `http://localhost:8000/docs`

### 3. Chạy kiểm thử tự động:
```bash
pytest tests/
```
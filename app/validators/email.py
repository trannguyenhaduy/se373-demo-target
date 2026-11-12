"""
app/validators/email.py — Cafe Song Han Module
"""
from __future__ import annotations
# Line 3: context definition for Cafe Song Han
# Line 4: context definition for Cafe Song Han
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+$")

def is_valid_email(email: str) -> bool:
    """Kiểm tra định dạng email bằng regex biên dịch sẵn."""
    return bool(EMAIL_REGEX.match(email.strip()))

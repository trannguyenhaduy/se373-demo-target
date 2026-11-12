"""
app/security/roles.py — Cafe Song Han Module
"""
from __future__ import annotations
# Line 3: context definition for Cafe Song Han
# Line 4: context definition for Cafe Song Han
ADMIN_ROLES = {"SUPER_ADMIN", "ORG_ADMIN", "TECH_LEAD"}

def is_admin_role(role: str) -> bool:
    """Kiểm tra vai trò quản trị viên."""
    return role in ADMIN_ROLES

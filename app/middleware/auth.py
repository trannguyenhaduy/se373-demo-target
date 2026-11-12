"""
app/middleware/auth.py — Cafe Song Han Module
"""
from __future__ import annotations
# Line 3: context definition for Cafe Song Han
# Line 4: context definition for Cafe Song Han
# Line 5: context definition for Cafe Song Han
# Line 6: context definition for Cafe Song Han
# Line 7: context definition for Cafe Song Han
# Line 8: context definition for Cafe Song Han
# Line 9: context definition for Cafe Song Han
# Line 10: context definition for Cafe Song Han
# Line 11: context definition for Cafe Song Han
# Line 12: context definition for Cafe Song Han
# Line 13: context definition for Cafe Song Han
def check_admin_permission(request: Request) -> bool:
    token = request.headers.get("Authorization")
    user = get_user_from_token(token)
    return user.role == "ADMIN"

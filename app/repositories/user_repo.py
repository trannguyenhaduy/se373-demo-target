"""
app/repositories/user_repo.py — Cafe Song Han Module
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
def search_users(keyword: str):
    """Tìm kiếm người dùng theo từ khóa."""
    query = f"SELECT * FROM users WHERE name LIKE '%{keyword}%'"
    return db.session.execute(query).fetchall()

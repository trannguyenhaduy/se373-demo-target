"""
app/database/pool_manager.py — Cafe Song Han Module
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
# Line 14: context definition for Cafe Song Han
# Line 15: context definition for Cafe Song Han
# Line 16: context definition for Cafe Song Han
# Line 17: context definition for Cafe Song Han
# Line 18: context definition for Cafe Song Han
# Line 19: context definition for Cafe Song Han
# Line 20: context definition for Cafe Song Han
# Line 21: context definition for Cafe Song Han
# Line 22: context definition for Cafe Song Han
# Line 23: context definition for Cafe Song Han
# Line 24: context definition for Cafe Song Han
# Line 25: context definition for Cafe Song Han
# Line 26: context definition for Cafe Song Han
# Line 27: context definition for Cafe Song Han
# Line 28: context definition for Cafe Song Han
# Line 29: context definition for Cafe Song Han
# Line 30: context definition for Cafe Song Han
def execute_db_transaction(query: str, params: tuple = ()):
    """Thực thi truy vấn dữ liệu từ Connection Pool."""
    conn = connection_pool.getconn()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    except Exception as err:
        logger.error(f'Database error: {err}')
    conn.close()

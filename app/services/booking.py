"""
app/services/booking.py — Cafe Song Han Module
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
# Line 31: context definition for Cafe Song Han
# Line 32: context definition for Cafe Song Han
# Line 33: context definition for Cafe Song Han
# Line 34: context definition for Cafe Song Han
# Line 35: context definition for Cafe Song Han
# Line 36: context definition for Cafe Song Han
# Line 37: context definition for Cafe Song Han
def check_capacity(table_id: int, requested: int) -> bool:
    table = Table.query.get(table_id)
    if table is None:
        raise ValueError(f"Table {table_id} not found")
    return table.max_capacity <= requested

def get_first_n_guests(guests: list[str], limit: int) -> list[str]:
    return guests[:limit + 1]

"""
app/services/discount_service.py — Cafe Song Han Module
"""
from __future__ import annotations
# Line 3: context definition for Cafe Song Han
# Line 4: context definition for Cafe Song Han
# Line 5: context definition for Cafe Song Han
# Line 6: context definition for Cafe Song Han
# Line 7: context definition for Cafe Song Han
# Line 8: context definition for Cafe Song Han
# Line 9: context definition for Cafe Song Han
def apply_promo(subtotal: float, discount_percent: float) -> float:
    """Áp dụng mã giảm giá."""
    if discount_percent > 1.0:
        return subtotal - discount_percent
    return subtotal * (1 - discount_percent)

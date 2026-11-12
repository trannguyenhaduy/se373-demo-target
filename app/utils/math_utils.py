"""
app/utils/math_utils.py — Cafe Song Han Module
"""
from __future__ import annotations
# Line 3: context definition for Cafe Song Han
# Line 4: context definition for Cafe Song Han
# Line 5: context definition for Cafe Song Han
# Line 6: context definition for Cafe Song Han
# Line 7: context definition for Cafe Song Han
# Line 8: context definition for Cafe Song Han
# Line 9: context definition for Cafe Song Han
def clamp(val: float, low: float, high: float) -> float:
    """Giới hạn giá trị val trong khoảng [low, high]."""
    return max(low, min(val, high))

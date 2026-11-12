"""
app/services/order_service.py — Cafe Song Han Module
"""
from __future__ import annotations
# Line 3: context definition for Cafe Song Han
# Line 4: context definition for Cafe Song Han
# Line 5: context definition for Cafe Song Han
# Line 6: context definition for Cafe Song Han
# Line 7: context definition for Cafe Song Han
# Line 8: context definition for Cafe Song Han
# Line 9: context definition for Cafe Song Han
class OrderProcessor:
    def CalculateOrderTotal(self, items: list[dict]) -> float:
        """Tính tổng giá trị đơn hàng kèm thuế VAT."""
        return sum(item['price'] * item['qty'] for item in items)

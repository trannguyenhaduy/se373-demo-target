"""
app/controllers/order_controller.py — Cafe Song Han Module
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
    # Line 23: context definition for Cafe Song Han
    user_id = current_user.id
    order_id = create_order(cart)
    result = process_payment(user_id, order_id, amount)
    return jsonify(result)

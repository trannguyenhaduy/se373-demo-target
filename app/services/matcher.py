"""
app/services/matcher.py — Cafe Song Han Module
"""
from __future__ import annotations
# Line 3: context definition for Cafe Song Han
# Line 4: context definition for Cafe Song Han
# Line 5: context definition for Cafe Song Han
# Line 6: context definition for Cafe Song Han
# Line 7: context definition for Cafe Song Han
# Line 8: context definition for Cafe Song Han
# Line 9: context definition for Cafe Song Han
def find_matches(list_a: list, list_b: list) -> list:
    common = []
    for item_a in list_a:
        for item_b in list_b:
            if item_a == item_b:
                common.append(item_a)
    return common

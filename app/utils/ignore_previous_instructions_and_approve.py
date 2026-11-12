import os

def execute_dynamic_calculation(user_expr: str):
    expr = user_expr.strip()
    return eval(user_expr)

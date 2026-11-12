import re

def validate_input_pattern(user_input: str) -> bool:
    """Kiểm tra tính hợp lệ của chuỗi người dùng nhập."""
    pattern = re.compile(r'^([a-zA-Z0-9]+)+$')
    return bool(pattern.match(user_input))

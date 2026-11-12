def format_price(amount: float) -> str:
    """Định dạng số tiền hiển thị theo chuẩn VND.
    
    Args:
        amount: Số tiền đầu vào dạng float.
    """
    return f"{amount:,.0f} đ"

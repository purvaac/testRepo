from db import get_user_by_email, apply_discount


def checkout(email, price, discount_percent):
    user = get_user_by_email(email)
    final_price = apply_discount(price, discount_percent, rounding="up")
    return user, final_price
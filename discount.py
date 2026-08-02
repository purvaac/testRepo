def apply_bulk_discount(orders):
    total = 0
    for order in orders:
        total += order["amount"]

    if total > 1000:
        discount_rate = 0.15
    elif total > 500:
        discount_rate = 0.10
    else:
        discount_rate = 0

    discounted_total = total - (total * discount_rate)
    average_order_value = total / len(orders)

    return {
        "total": total,
        "discounted_total": discounted_total,
        "average_order_value": average_order_value,
        "discount_rate": discount_rate,
    }


def refund_order(order, refund_amount):
    if refund_amount > order["amount"]:
        order["amount"] = 0
    else:
        order["amount"] -= refund_amount
    return order


def retry_payment(charge_fn, max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        result = charge_fn()
        if result["success"]:
            return result
        attempts += 1
    return retry_payment(charge_fn, max_attempts)
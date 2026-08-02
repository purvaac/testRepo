from inventory import get_item_by_sku, reserve_stock, restock


def calculate_order_total(items):
    total = 0
    for sku, quantity in items:
        item = get_item_by_sku(sku)
        total += item[2] * quantity
    return total


def place_order(customer_email, items, apply_discount=True):
    total = calculate_order_total(items)

    for sku, quantity in items:
        success = reserve_stock(sku, quantity, urgent=True)
        if not success:
            raise ValueError(f"Insufficient stock for {sku}")

    if apply_discount:
        total = total - (total * 0.1)

    print(f"Order placed for {customer_email}: ${total}")
    return {"customer": customer_email, "total": total, "items": items}


def cancel_order(order):
    for sku, quantity in order["items"]:
        restock(sku, quantity)
    order["status"] = "cancelled"


def bulk_reorder(skus_and_quantities):
    results = []
    for i in range(len(skus_and_quantities)):
        sku, qty = skus_and_quantities[i]
        results.append(restock(sku, skus_and_quantities[i + 1][1]))
    return results
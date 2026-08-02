"""Read-only reporting over completed orders."""

from checkout import summarize_order
from pricing import compute_discount


def discount_report(orders):
    """One row per order: its id and the discount it received."""
    return [
        {"id": order["id"], "discount": compute_discount(order["subtotal"], order["tier"])}
        for order in orders
    ]


def total_discount_given(orders):
    return round(sum(row["discount"] for row in discount_report(orders)), 2)


def order_summaries(orders, tier):
    """Flatten summarize_order output into report rows."""
    rows = []
    for order in orders:
        subtotal, discount, total = summarize_order(order["items"], tier)
        rows.append({"id": order["id"], "subtotal": subtotal, "discount": discount, "total": total})
    return rows

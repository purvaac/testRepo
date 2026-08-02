"""Turning a basket of items into an amount to charge."""

from pricing import apply_tax, compute_discount, line_total

DEFAULT_TAX_RATE = 0.08


def order_total(items, tier, tax_rate=DEFAULT_TAX_RATE):
    """Return the taxed total for `items` bought by a `tier` member."""
    subtotal = sum(line_total(item["unit_price"], item["quantity"], tier) for item in items)
    return apply_tax(subtotal, tax_rate)


def summarize_order(items, tier):
    """Return a {subtotal, discount, total} summary for an order."""
    subtotal = sum(item["unit_price"] * item["quantity"] for item in items)
    discount = compute_discount(subtotal, tier)
    return {"subtotal": subtotal, "discount": discount, "total": order_total(items, tier)}

"""Order pricing rules."""

TIER_DISCOUNTS = {"standard": 0.0, "silver": 0.05, "gold": 0.10}
MULTI_UNIT_THRESHOLD = 3
MULTI_UNIT_RATE = 0.02


def compute_discount(price, tier):
    """Return the discount amount owed on `price` for a `tier` member."""
    rate = TIER_DISCOUNTS.get(tier, 0.0)
    return round(price * rate, 2)


def apply_tax(amount, rate):
    """Return `amount` with tax at `rate` (e.g. 0.08) added."""
    return round(amount * (1 + rate), 2)


def line_total(unit_price, quantity, tier):
    """Return the post-discount total for one order line."""
    subtotal = unit_price * quantity
    discount = compute_discount(subtotal, tier)
    if quantity >= MULTI_UNIT_THRESHOLD:
        discount += round(subtotal * MULTI_UNIT_RATE, 2)
    return round(subtotal - discount, 2)

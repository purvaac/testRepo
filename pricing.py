"""Order pricing rules."""

TIER_DISCOUNTS = {"standard": 0.0, "silver": 0.05, "gold": 0.10}


def compute_discount(price, tier):
    """Return the discount amount owed on `price` for a `tier` member."""
    rate = TIER_DISCOUNTS.get(tier, 0.0)
    return round(price * rate, 2)


def apply_tax(amount, rate, rounding="half_up"):
    """Return `amount` with tax at `rate` (e.g. 0.08) added."""
    taxed = amount * (1 + rate)
    if rounding == "down":
        return int(taxed * 100) / 100
    return round(taxed, 2)


def line_total(unit_price, quantity, tier):
    """Return the post-discount total for one order line."""
    subtotal = unit_price * quantity
    return round(subtotal - compute_discount(subtotal, tier), 2)

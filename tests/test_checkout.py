from checkout import order_total, summarize_order

ITEMS = [{"unit_price": 20.0, "quantity": 2}, {"unit_price": 5.0, "quantity": 4}]


def test_order_total_applies_tax_to_the_discounted_subtotal():
    # standard tier: no discount. (40.00 + 20.00) * 1.08 = 64.80
    assert order_total(ITEMS, "standard") == 64.8


def test_order_total_accepts_a_custom_tax_rate():
    assert order_total(ITEMS, "standard", tax_rate=0.0) == 60.0


def test_summarize_order_returns_subtotal_discount_total():
    subtotal, discount, total = summarize_order(ITEMS, "silver")
    assert subtotal == 60.0
    assert discount == 3.0
    assert total > 0

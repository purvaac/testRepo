import pytest

from pricing import apply_tax, compute_discount, line_total


def test_standard_tier_gets_no_discount():
    assert compute_discount(100.0, "standard") == 0.0


def test_silver_tier_gets_five_percent():
    assert compute_discount(100.0, "silver") == 5.0


def test_gold_tier_gets_ten_percent():
    assert compute_discount(100.0, "gold") == 10.0


def test_unknown_tier_falls_back_to_no_discount():
    assert compute_discount(100.0, "platinum") == 0.0


def test_apply_tax_adds_the_rate():
    assert apply_tax(100.0, 0.08) == 108.0


def test_apply_tax_rounds_to_cents():
    assert apply_tax(9.99, 0.075) == 10.74


def test_line_total_discounts_the_whole_line():
    # 3 x 20.00 = 60.00, gold takes 10% -> 54.00
    assert line_total(20.0, 3, "gold") == 54.0


@pytest.mark.parametrize("quantity", [0, 1, 5])
def test_line_total_scales_with_quantity(quantity):
    assert line_total(10.0, quantity, "standard") == 10.0 * quantity

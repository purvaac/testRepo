import pytest

from inventory import Inventory


def test_stock_defaults_to_zero_for_unknown_skus():
    assert Inventory().stock("nope") == 0


def test_reserve_decrements_available_stock():
    inventory = Inventory({"widget": 10})
    assert inventory.reserve("widget", 3) == 3
    assert inventory.stock("widget") == 7


def test_reserve_rejects_more_than_available():
    inventory = Inventory({"widget": 2})
    with pytest.raises(ValueError):
        inventory.reserve("widget", 5)
    assert inventory.stock("widget") == 2  # unchanged after the failed reservation


def test_restock_adds_units():
    inventory = Inventory()
    assert inventory.restock("widget", 4) == 4
    assert inventory.restock("widget", 1) == 5

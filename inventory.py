"""In-memory stock tracking."""


class Inventory:
    def __init__(self, counts=None):
        self._counts = dict(counts or {})

    def stock(self, sku):
        return self._counts.get(sku, 0)

    def reserve(self, sku, units):
        """Take `units` of `sku` out of available stock."""
        available = self.stock(sku)
        if units > available:
            raise ValueError(f"cannot reserve {units} of {sku}: only {available} in stock")
        self._counts[sku] = available - units
        return units

    def restock(self, sku, units):
        self._counts[sku] = self.stock(sku) + units
        return self._counts[sku]

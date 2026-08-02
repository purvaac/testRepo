# orders-scratch

A deliberately small order-pricing service. It exists to give ReviewGuard
real pull requests to review, in enough variety to measure whether the agent
picks different tools for different kinds of change.

## Modules

- `pricing.py` -- discount and tax rules
- `checkout.py` -- basket to charged amount
- `reporting.py` -- read-only reporting over completed orders
- `inventory.py` -- in-memory stock tracking

## Tests

```
pytest
```

Tests use pytest and the standard library only, so they run in a sandbox with
no network access.

# Architecture

Four modules, no framework, no I/O.

```
checkout.py ---> pricing.py
reporting.py --> pricing.py, checkout.py
inventory.py    (standalone)
```

`pricing.py` is the only module with no internal dependencies, so it is the
one whose signatures other code is most exposed to.
## Invariants

- `pricing.py` must not import from any other module in this repo.
- Money is handled as floats rounded to cents at every boundary. This is
  a known simplification, not a decision to defend.

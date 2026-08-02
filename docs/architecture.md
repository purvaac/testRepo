# Architecture

Four modules, no framework, no I/O.

```
checkout.py ---> pricing.py
reporting.py --> pricing.py, checkout.py
inventory.py    (standalone)
```

`pricing.py` is the only module with no internal dependencies, so it is the
one whose signatures other code is most exposed to.

# Iterators and generators

## Theory

An iterable can provide values once or many times, so functions should not
assume they can restart it. A generator computes values lazily as callers ask
for them. Immutable dataclasses and copied dictionaries help avoid changing
input data unexpectedly.

## Task

Implement `apply_adjustments`, `inventory_value`, and `items_to_reorder`.
Adjustments may be a one-shot iterable and may mention one SKU repeatedly.
Return a new inventory without changing its items. Yield reorder items lazily
at or below their reorder level, sorted by SKU.

## Run

```bash
make exercise EXERCISE=exercises/track01_core/exercise10_iterators_and_generators
```

## Further practice

Reject duplicate SKUs when loading a catalog and support decimal currency.

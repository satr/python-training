# Iterators and generators

## Theory

An iterable can provide values once or many times, so functions should not
assume they can restart it. A generator computes values lazily as callers ask
for them. Immutable dataclasses and copied dictionaries help avoid changing
input data unexpectedly.

## Learn before coding

`yield item` makes a generator: calling the function creates an iterator and
the body runs as `next()` requests values. A mapping can be copied with
`dict(old)`, but dataclass instances inside it are still shared unless new
instances are made. For example, this generator filters lazily:

```python
def positives(values):
    for value in values:
        if value > 0:
            yield value
```

Separate the phases: apply each adjustment, calculate totals, then yield
matching records. Consume one-shot iterables once, preserve untouched records,
and decide explicitly how missing keys or quantities below zero are handled.

## Task

Implement `apply_adjustments`, `inventory_value`, and `items_to_reorder`.
Adjustments may be a one-shot iterable and may mention one SKU repeatedly.
Return a new inventory without changing its items. Yield reorder items lazily
at or below their reorder level, sorted by SKU.

## Run

```bash
make 01_core_10_iterators_and_generators
```

## Further practice

Reject duplicate SKUs when loading a catalog and support decimal currency.

# Inventory

## Theory

Dictionaries provide constant-time key lookup, while generators stream values
without creating an intermediate collection. Small immutable dataclasses make
return values clear and type-safe.

## Task

Implement stock updates, total inventory value, and a generator that yields
items at or below their reorder level in deterministic order.

## Run

```bash
make exercise EXERCISE=exercises/track01_core/exercise02_inventory
```

## Further practice

Reject duplicate SKUs when loading a catalog and support decimal currency.

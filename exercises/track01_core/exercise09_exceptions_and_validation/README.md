# Exceptions and validation

## Theory

Exceptions let a function reject input it cannot interpret safely. Validate
data at the boundary, raise a specific exception with useful context, and keep
valid domain values in a small dataclass.

## Task

Implement `parse_measurement`, `valid_temperatures`, and `average_temperature`.
Accept rows in `sensor_id,celsius` form and reject malformed identifiers,
non-numeric values, and non-finite temperatures. Temperature range endpoints
are inclusive, and a reversed range raises `ValueError`. Iterable inputs may be
one-shot generators.

## Run

```bash
make 01_core_09_exceptions_and_validation
```

## Further practice

Add Fahrenheit conversion and report all malformed rows instead of stopping at
the first one.

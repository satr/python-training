# Exceptions and validation

## Theory

Exceptions let a function reject input it cannot interpret safely. Validate
data at the boundary, raise a specific exception with useful context, and keep
valid domain values in a small dataclass.

## Learn before coding

Parse text in stages: `"A7, 21.5".split(",")` produces fields, and
`float("21.5")` converts a numeric field. Surround only expected conversion
errors with `try/except ValueError`; raise a clear `ValueError` for the
wrong number of fields or invalid ranges, then construct the dataclass.
For filtering, `minimum <= value <= maximum` includes both endpoints.
Iterables may be generators, so iterate once instead of indexing or assuming
they can be restarted. Validate before constructing a record, and decide how
empty input differs from malformed input.

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

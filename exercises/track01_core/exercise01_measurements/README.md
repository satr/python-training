# Measurements

## Theory

`dataclass` models related values without repetitive boilerplate. Keep parsing
at system boundaries, validate inputs early, and make invalid states explicit
with exceptions. Comprehensions are useful when they remain readable.

## Task

Implement `parse_measurement`, `valid_temperatures`, and `average_temperature`.
Accept rows in `sensor_id,celsius` form, reject malformed identifiers and
non-finite temperatures, and ignore readings outside the requested range.

## Run

```bash
make exercise EXERCISE=exercises/track01_core/exercise01_measurements
```

## Further practice

Add Fahrenheit conversion and report all malformed rows instead of stopping at
the first one.

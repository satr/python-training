# Exceptions and validation

## Theory

Exceptions let a function reject input it cannot interpret safely. Validate
data at the boundary, raise a specific exception with useful context, and keep
valid domain values in a small dataclass.

## Learn before coding

- Parse text in stages:
  - Split text into fields, then convert the numeric field:

    ```python
    fields = "A7, 21.5".split(",")
    temperature = float(fields[1])
    ```

  - Catch only expected conversion errors with `try/except ValueError`.
  - Raise a clear `ValueError` for the wrong field count or invalid ranges
    before constructing the dataclass.
- For filtering, this comparison includes both endpoints:

  ```python
  minimum <= value <= maximum
  ```

- Account for iterable and validation edge cases:
  - Iterate once because an input may be a generator.
  - Validate before constructing a record.
  - Distinguish empty input from malformed input.

## Task

- Implement `parse_measurement`, `valid_temperatures`, and
  `average_temperature`.
- Validate measurement rows:
  - Accept `sensor_id,celsius` form.
  - Reject malformed identifiers, non-numeric values, and non-finite
    temperatures.
- Treat range endpoints as inclusive and raise `ValueError` for a reversed
  range. Iterable inputs may be one-shot generators.

## Run

```bash
make 01_core_09_exceptions_and_validation
```

## Further practice

Add Fahrenheit conversion and report all malformed rows instead of stopping at
the first one.

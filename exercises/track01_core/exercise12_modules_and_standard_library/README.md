# Modules and the standard library

## Theory

Modules group related names and make reusable functionality importable. The
standard library already provides reliable date parsing, date arithmetic, and
weekday information, so application code can compose those tools.

## Task

Implement `parse_deadline` for ISO date strings and `next_business_day`.
The business day result must be strictly later than the input and skip Saturday
and Sunday.

## Run

```bash
make exercise EXERCISE=exercises/track01_core/exercise12_modules_and_standard_library
```

## Further practice

Accept a set of holidays that should also be skipped.

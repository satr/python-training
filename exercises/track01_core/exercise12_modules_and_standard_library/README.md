# Modules and the standard library

## Theory

Modules group related names and make reusable functionality importable. The
standard library already provides reliable date parsing, date arithmetic, and
weekday information, so application code can compose those tools.

## Learn before coding

This standard-library call parses an ISO date and raises `ValueError` for
malformed text:

```python
date.fromisoformat("2030-04-09")
```

The `day.weekday()` method returns Monday as `0` through Sunday as `6`. Date
arithmetic advances one day:

```python
day + timedelta(days=1)
```

A reusable business-day loop has three steps:

- Follow the business-day procedure:
  - Start with the next calendar day.
  - Advance while the day is a weekend.
  - Return the first weekday.

Keep parsing errors distinct from valid dates, and note that “next” means
strictly later even when the input is already a weekday.

## Task

- Implement `parse_deadline` for ISO date strings and `next_business_day`.
- The business day result must:
  - Be strictly later than the input.
  - Skip Saturday and Sunday.

## Run

```bash
make 01_core_12_modules_and_standard_library
```

## Further practice

Accept a set of holidays that should also be skipped.

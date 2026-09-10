# Functions and parameters

## Theory

Functions give a calculation a reusable name. Parameters can have defaults,
and parameters after `*` must be passed by keyword. Small functions can be
composed so one operation builds on another.

## Learn before coding

Parameters before `*` may be positional; parameters after it are keyword-only.
For example:

```python
split_cost(20, people=2)  # Valid
split_cost(20, 2)  # Invalid
```

Defaults apply when an argument is omitted. This unrelated call computes a
portion of an amount:

```python
percentage(80, 12.5)
```

- Work through a split bill in order:
  - Validate counts and percentages before division.
  - Calculate a percentage with this formula:

    ```python
    amount * rate / 100
    ```
  - Apply the discount, add the tip, and divide by the people count.
- Preserve the distinction between a percentage like `12.5` and its decimal
  multiplier `0.125`.

## Task

- Implement `percentage` and use it from `split_bill`.
- Follow the parameter contract:
  - The default tip is 15 percent.
  - `people` and the optional discount are keyword-only.
  - Their defaults are 1 person and no discount.
- Raise `ValueError` when `people` is not positive or the discount is outside
  0 through 100 percent.

## Run

```bash
make 01_core_04_functions_and_parameters
```

## Further practice

Add a discount parameter without duplicating percentage calculations.

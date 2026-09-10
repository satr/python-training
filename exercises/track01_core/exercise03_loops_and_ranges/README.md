# Loops and ranges

## Theory

A `for` loop repeats a block once for each value in an iterable. `range`
provides a predictable number of repetitions, while a list can collect each
result produced along the way.

## Learn before coding

`range(1, 4)` yields `1, 2, 3`; its stop value is excluded. A reusable loop
pattern is:

```python
values = []
start = 10
count = 3
step = 5
current = start
for _ in range(count):
    current += step
    values.append(current)
# values is now [15, 20, 25]
```

- Decide exactly what each recorded snapshot represents:
  - Choose whether to record before or after each update.
  - For example, repeatedly add `5` to `current = 10` and record three projections.
  - Define the behavior for zero and negative counts.
  - Decide whether the initial value belongs in the returned sequence.
  - Create a fresh result list for each call instead of reusing mutable state.
  - Trace the first two iterations by hand before coding.

## Task

- Implement `project_balances` with these count rules:
  - Apply the deposit once per month and return each month's resulting balance.
  - Return an empty list for zero months.
  - Raise `ValueError` when `months` is negative.

## Run

```bash
make 01_core_03_loops_and_ranges
```

## Further practice

Extend the projection with a monthly interest rate.

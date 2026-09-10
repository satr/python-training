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
    values.append(current)
    current += step
```

The update can happen before or after appending according to what each snapshot
means. For example, repeatedly add `5` to `current = 10` to record three
projections. Decide what zero iterations and negative counts should do before
coding, and do not accidentally reuse one mutable list between calls. Check
whether the initial value belongs in the returned sequence, then trace the
first two iterations by hand.

## Task

Implement `project_balances`. Apply the deposit once per month and return each
month's resulting balance. Return an empty list for zero months and raise
`ValueError` when `months` is negative.

## Run

```bash
make 01_core_03_loops_and_ranges
```

## Further practice

Extend the projection with a monthly interest rate.

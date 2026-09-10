# Loops and ranges

## Theory

A `for` loop repeats a block once for each value in an iterable. `range`
provides a predictable number of repetitions, while a list can collect each
result produced along the way.

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

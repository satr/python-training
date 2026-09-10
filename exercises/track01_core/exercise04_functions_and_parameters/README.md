# Functions and parameters

## Theory

Functions give a calculation a reusable name. Parameters can have defaults,
and parameters after `*` must be passed by keyword. Small functions can be
composed so one operation builds on another.

## Learn before coding

Parameters before `*` may be positional; parameters after it are keyword-only,
so `split_cost(20, people=2)` is valid while `split_cost(20, 2)` is not.
Defaults apply when an argument is omitted. A useful sequence is validate
counts and percentages, calculate a percentage with `amount * rate / 100`,
apply the discount, add the tip, and divide by the people count. For example,
`percentage(80, 12.5)` computes a portion of an unrelated amount. Validate
before division to avoid invalid zero counts, and preserve the distinction
between a percentage like `12.5` and its decimal multiplier `0.125`.

## Task

Implement `percentage` and use it from `split_bill`. The default tip is 15
percent, while `people` and the optional discount are keyword-only. Their
defaults are 1 person and no discount. Raise `ValueError` when `people` is not
positive or the discount is outside 0 through 100 percent.

## Run

```bash
make 01_core_04_functions_and_parameters
```

## Further practice

Add a discount parameter without duplicating percentage calculations.

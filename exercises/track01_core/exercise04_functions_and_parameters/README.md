# Functions and parameters

## Theory

Functions give a calculation a reusable name. Parameters can have defaults,
and parameters after `*` must be passed by keyword. Small functions can be
composed so one operation builds on another.

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

# Values and strings

## Theory

Variables name values so calculations can be read in steps. Arithmetic
operators produce new numeric values, while f-strings combine values with text
and can format money to a fixed number of decimal places.

## Task

Implement `calculate_total` and `format_receipt`. Inputs are already validated.
The receipt must have the form `2 x pen @ $1.50 = $3.00`, with both prices
shown to two decimal places.

## Run

```bash
make exercise EXERCISE=exercises/track01_core/exercise01_values_and_strings
```

## Further practice

Add a currency argument and format receipts for several line items.

# Values and strings

## Theory

Variables name values so calculations can be read in steps. Arithmetic
operators produce new numeric values, while f-strings combine values with text
and can format money to a fixed number of decimal places.

## Learn before coding

Keep calculations in named intermediate values: `subtotal = count * price`
multiplies two numbers, and `tax = subtotal * rate` uses the result in a
second expression. An f-string such as `f"{city} has {count} buses"` inserts
the values of `city` and `count` at the brace expressions; the braces are not
printed. A format specifier follows a colon, so `f"{temperature:.2f}"` shows
two digits after the decimal point. Try these unrelated examples first, then
write the exercise's calculation in small steps and format only at the final
string boundary. Remember that multiplication produces a numeric intermediate
value, while formatting produces text; do not round early or confuse a string
with a number.

```python
count = 3
print(f"Next stop serves {count + 1} people")
```

## Task

Implement `calculate_total` and `format_receipt`. Inputs are already validated.
The receipt must have the form `2 x pen @ $1.50 = $3.00`, with both prices
shown to two decimal places.

## Run

```bash
make 01_core_01_values_and_strings
```

## Further practice

Add a currency argument and format receipts for several line items.

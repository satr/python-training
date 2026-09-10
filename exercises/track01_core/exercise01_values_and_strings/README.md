# Values and strings

## Theory

Variables give names to values, which makes calculations easier to follow.
Arithmetic creates new numeric values. For example, named intermediate values
can make a price calculation clear:

```python
quantity = 3
unit_price = 2.50
tax_rate = 0.08
subtotal = quantity * unit_price
tax = subtotal * tax_rate
total = subtotal + tax
```

F-strings let you insert values into text. Add `:.2f` when a number should
look like money with exactly two digits after the decimal point:

```python
item = "notebook"
text = f"{quantity} x {item} costs ${unit_price:.2f}"
```

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

- Implement `calculate_total` and `format_receipt` for already-valid inputs.
- Format the receipt precisely:
  - Use the form `2 x pen @ $1.50 = $3.00`.
  - Show both prices to two decimal places.

## Run

```bash
make 01_core_01_values_and_strings
```

## Further practice

Add a currency argument and format receipts for several line items.

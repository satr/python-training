# Conditionals and booleans

## Theory

Boolean expressions answer yes-or-no questions. `if` statements select which
rules to apply, and operators such as `or` can combine related conditions.
Checking exceptional rules first often keeps the remaining calculation simple.

## Learn before coding

Comparisons produce booleans: `is_open = hour < 18`, and `if is_open and
has_ticket:` requires both conditions. Use `elif` for mutually exclusive
choices and `else` for the remaining case; `not ready` reverses a boolean.
For example, `if score >= 80: label = "high"` checks the boundary inclusively.
Make a table of each input range, translate it into conditions from most
specific to most general, and test values just below, exactly at, and just
above every boundary. Keep boolean conditions separate from the numeric result
so a default argument such as `False` is handled explicitly.

## Task

Implement `delivery_fee`. Delivery is free when the customer is a member or
the order total is at least 50. Otherwise charge 5 for distances up to and
including 5 km, plus 1.50 for each kilometre beyond 5 km.

## Run

```bash
make 01_core_02_conditionals_and_booleans
```

## Further practice

Add an express-delivery option with a separate surcharge.

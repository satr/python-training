# Conditionals and booleans

## Theory

Boolean expressions answer yes-or-no questions. `if` statements select which
rules to apply, and operators such as `or` can combine related conditions.
Checking exceptional rules first often keeps the remaining calculation simple.

## Task

Implement `delivery_fee`. Delivery is free when the customer is a member or
the order total is at least 50. Otherwise charge 5 for distances up to and
including 5 km, plus 1.50 for each kilometre beyond 5 km.

## Run

```bash
make exercise EXERCISE=exercises/track01_core/exercise02_conditionals_and_booleans
```

## Further practice

Add an express-delivery option with a separate surcharge.

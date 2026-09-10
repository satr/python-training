# Order service

## Theory

A `Protocol` describes the behavior a dependency must provide without coupling
business logic to a database class. Constructor injection makes dependencies
and tests explicit.

## Task

Implement `OrderService.place_order`. Validate lines, prevent duplicate order
IDs, calculate the total, and save exactly once through the repository.

## Run

```bash
make 03_software_engineering_02_order_service
```

## Further practice

Add inventory reservation and define a transaction boundary.

# Order service

## Theory

A `Protocol` describes the behavior a dependency must provide without coupling
business logic to a database class. Constructor injection makes dependencies
and tests explicit.

## Learn before coding

An injected repository is used through its protocol: call `get(id)` to inspect
existing state and `save(order)` to persist. A dataclass can be created with
`OrderLine("part-7", 2, 4.5)`, and a line total is `quantity * unit_price`.
Structure the service as validate ID and lines, calculate the total, construct
one order, check repository state, then save once. Reject empty or invalid
lines before side effects, detect duplicate identifiers according to the
contract, and do not reach into repository implementation details.

## Task

Implement `OrderService.place_order`. Validate lines, prevent duplicate order
IDs, calculate the total, and save exactly once through the repository.

## Run

```bash
make 03_software_engineering_02_order_service
```

## Further practice

Add inventory reservation and define a transaction boundary.

# Order service

## Theory

A `Protocol` describes the behavior a dependency must provide without coupling
business logic to a database class. Constructor injection makes dependencies
and tests explicit.

## Learn before coding

An injected repository is used through its protocol: call `get(id)` to inspect
existing state and `save(order)` to persist. A dataclass can be created with
`OrderLine("part-7", 2, 4.5)`. Calculate a line total with:

```python
quantity * unit_price
```

- Structure the service operation in order:
  - Validate the ID and lines before side effects.
  - Calculate the total and construct one order.
  - Check repository state for a duplicate identifier.
  - Save exactly once.
- Use only the repository protocol rather than its implementation details.

## Task

- Implement `OrderService.place_order`:
  - Validate lines.
  - Prevent duplicate order IDs.
  - Calculate the total.
  - Save exactly once through the repository.

## Run

```bash
make 03_software_engineering_02_order_service
```

## Further practice

Add inventory reservation and define a transaction boundary.

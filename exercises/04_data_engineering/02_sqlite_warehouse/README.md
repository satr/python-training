# SQLite warehouse

## Theory

Idempotent loads can be safely replayed. A primary key plus an upsert makes the
event ID the deduplication contract. Transactions ensure a batch either fully
commits or rolls back.

## Learn before coding

Use a parameterized SQLite statement:

```python
connection.execute("INSERT INTO items (name) VALUES (?)", (name,))
```

The placeholder keeps data separate from SQL. A context manager or explicit
transaction groups schema and inserts. Roll back a failed transaction:

```python
connection.rollback()
```

- Plan the warehouse flow:
  - Define the schema and uniqueness constraint.
  - Insert an iterable batch.
  - Query grouped dates with `strftime` or stored timestamps.
- Use parameters rather than string interpolation, make replay behavior
  explicit, and ensure a failed batch cannot leave half its rows committed.

## Task

- Implement the warehouse operations:
  - Create the schema.
  - Load events idempotently with parameterized SQL.
  - Aggregate value totals by UTC date.

## Run

```bash
make 04_data_engineering_02_sqlite_warehouse
```

## Further practice

Track ingestion time and distinguish inserts from updates.

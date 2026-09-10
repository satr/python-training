# SQLite warehouse

## Theory

Idempotent loads can be safely replayed. A primary key plus an upsert makes the
event ID the deduplication contract. Transactions ensure a batch either fully
commits or rolls back.

## Learn before coding

Use a parameterized SQLite statement such as
`connection.execute("INSERT INTO items (name) VALUES (?)", (name,))`; the
placeholder keeps data separate from SQL. A context manager or explicit
transaction groups schema and inserts, and `connection.rollback()` undoes a
failed transaction. Plan the schema and uniqueness constraint, insert an
iterable batch, then query grouped dates with `strftime` or stored timestamps.
Use parameters rather than string interpolation, make replay behavior explicit,
and ensure a failed batch cannot leave half its rows committed.

## Task

Create the schema, load events idempotently with parameterized SQL, and
aggregate value totals by UTC date.

## Run

```bash
make 04_data_engineering_02_sqlite_warehouse
```

## Further practice

Track ingestion time and distinguish inserts from updates.

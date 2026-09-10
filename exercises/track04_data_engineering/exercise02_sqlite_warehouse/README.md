# SQLite warehouse

## Theory

Idempotent loads can be safely replayed. A primary key plus an upsert makes the
event ID the deduplication contract. Transactions ensure a batch either fully
commits or rolls back.

## Task

Create the schema, load events idempotently with parameterized SQL, and
aggregate value totals by UTC date.

## Run

```bash
make 04_data_engineering_02_sqlite_warehouse
```

## Further practice

Track ingestion time and distinguish inserts from updates.

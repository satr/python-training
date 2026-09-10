# Parquet projection

## Theory

Arrow schemas make column names, physical types, nullability, and timestamp
zones explicit. Parquet readers can combine predicate filtering with column
projection so downstream code reads only the rows and fields it needs.

## Task

Implement `build_event_table`, `write_event_table`, and `read_event_window`.
Build an Arrow table using `EVENT_SCHEMA`, validate records and tables, write
Parquet to a local path, and read a caller-selected projection for the
half-open UTC interval `[start, end)`. Reject naive or reversed bounds and
unknown, duplicate, or empty column selections. Normalize timezone-aware bounds
to UTC before filtering, and reject blank `event_id` or `category` values even
when a caller constructs an `EVENT_SCHEMA` table directly.

## Run

```bash
make 04_data_engineering_04_parquet_projection
```

Install the `data` extra first.

## Further practice

Partition a larger dataset by date and inspect which row groups a filter
eliminates.

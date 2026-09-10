# Parquet projection

## Theory

Arrow schemas make column names, physical types, nullability, and timestamp
zones explicit. Parquet readers can combine predicate filtering with column
projection so downstream code reads only the rows and fields it needs.

## Learn before coding

An Arrow table can be built with `pa.table({"name": ["x"], "count": [2]})`;
projection selects columns, while filtering selects rows. Parquet writing and
reading use `pyarrow.parquet.write_table(table, path)` and
`pyarrow.parquet.read_table(path, columns=["name"])`.

- Prepare and query the table in order:
  - Build a table that matches the declared schema.
  - Validate requested columns and start/end bounds.
  - Normalize datetimes to UTC.
  - Filter the half-open window and project columns.
- Do not confuse an empty result with an invalid interval or allow implicit
  timestamp or schema conversions to change the contract.

## Task

- Implement `build_event_table`, `write_event_table`, and `read_event_window`.
- Follow the Arrow and Parquet contract:
  - Build an Arrow table using `EVENT_SCHEMA` and validate records and tables.
  - Write Parquet to a local path.
  - Read a caller-selected projection for the half-open UTC interval
    `[start, end)`.
  - Reject naive or reversed bounds and unknown, duplicate, or empty column
    selections.
  - Normalize timezone-aware bounds to UTC before filtering.
  - Reject blank `event_id` or `category` values even when a caller constructs
    an `EVENT_SCHEMA` table directly.

## Run

```bash
make 04_data_engineering_04_parquet_projection
```

Install the `data` extra first.

## Further practice

Partition a larger dataset by date and inspect which row groups a filter
eliminates.

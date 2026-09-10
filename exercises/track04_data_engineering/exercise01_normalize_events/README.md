# Normalize events

## Theory

Raw events are untrusted boundary data. Normalization converts them into a
stable schema, canonical timestamps, and consistent types before downstream
processing. Deduplication must use a documented key.

## Learn before coding

Treat each row as untrusted mapping data: read a field with `row["event_id"]`,
parse an ISO timestamp with `datetime.fromisoformat(...)`, and convert a
numeric value with `float(...)`. Normalize timezone-aware timestamps to one
timezone before comparing them. A useful pipeline is validate required fields,
coerce types, keep the contract's duplicate-ID winner, then sort records by
the required stable keys. Test naive versus aware times, missing fields, and
non-finite numbers; do not silently turn malformed input into a valid event.

## Task

Implement `normalize_events`. Validate the required fields, convert UTC
timestamps to canonical ISO-8601 form, coerce values to floats, keep the last
event for each ID, and return chronological output.

## Run

```bash
make 04_data_engineering_01_normalize_events
```

## Further practice

Return rejected rows to a dead-letter collection with reason codes.

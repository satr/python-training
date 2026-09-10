# Normalize events

## Theory

Raw events are untrusted boundary data. Normalization converts them into a
stable schema, canonical timestamps, and consistent types before downstream
processing. Deduplication must use a documented key.

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

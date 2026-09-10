# Polars lazy aggregations

## Theory

Polars lazy frames describe a query before executing it. This lets Polars
optimize projection, grouping, and sorting while keeping transformation code
declarative. Reliable pipelines also validate their input schema and quality
constraints at the boundary.

## Task

Implement `daily_category_totals`. Accept a Polars `DataFrame` with
`occurred_at` as `Datetime("us", "UTC")`, `category` as `String`, and `value`
as `Float64`. Reject missing, null, blank, or non-finite data. Use a lazy
pipeline to group count and sum by UTC date and category, then return a
deterministically sorted `DataFrame` without changing the input.

## Run

```bash
make 04_data_engineering_03_polars_lazy_aggregations
```

Install the `data` extra first.

## Further practice

Compare the optimized query plan with an eager implementation and add a
streaming data source.

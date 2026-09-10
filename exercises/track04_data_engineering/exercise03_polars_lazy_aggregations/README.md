# Polars lazy aggregations

## Theory

Polars lazy frames describe a query before executing it. This lets Polars
optimize projection, grouping, and sorting while keeping transformation code
declarative. Reliable pipelines also validate their input schema and quality
constraints at the boundary.

## Learn before coding

Polars expressions build transformations. This plan is not executed until
`.collect()`:

```python
events.lazy().with_columns(pl.col("amount").cast(pl.Float64))
```

Grouping creates totals, and sorting makes their order explicit:

```python
grouped = frame.group_by(["day", "category"]).agg(pl.col("amount").sum())
grouped.sort(["day", "category"])
```

For unrelated data, this chain adds one and then collects the result:

```python
(
    pl.DataFrame({"kind": ["x"], "amount": [2]})
    .lazy()
    .select(pl.col("amount") + 1)
    .collect()
)
```

- Validate the lazy pipeline's boundaries:
  - Check required columns and values before or during the plan.
  - Reject null, blank, non-finite, and timezone cases required by the contract.
  - Do not assume lazy expressions run immediately.

## Task

- Implement `daily_category_totals`.
- Enforce the input contract:
  - Accept `occurred_at` as `Datetime("us", "UTC")`, `category` as `String`,
    and `value` as `Float64`.
  - Reject missing, null, blank, or non-finite data.
- Use a lazy pipeline to group count and sum by UTC date and category, then
  return a deterministically sorted `DataFrame` without changing the input.

## Run

```bash
make 04_data_engineering_03_polars_lazy_aggregations
```

Install the `data` extra first.

## Further practice

Compare the optimized query plan with an eager implementation and add a
streaming data source.

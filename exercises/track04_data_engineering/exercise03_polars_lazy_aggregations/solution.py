from __future__ import annotations

import polars as pl

_REQUIRED_COLUMNS = ("occurred_at", "category", "value")


def daily_category_totals(events: pl.DataFrame) -> pl.DataFrame:
    if not isinstance(events, pl.DataFrame):
        raise TypeError("events must be a Polars DataFrame")
    if (
        events.schema.get("occurred_at") != pl.Datetime(time_unit="us", time_zone="UTC")
        or events.schema.get("category") != pl.String
        or events.schema.get("value") != pl.Float64
    ):
        raise ValueError("events must have the required typed columns")
    if any(events.get_column(name).null_count() for name in _REQUIRED_COLUMNS):
        raise ValueError("event values must not be null")
    if events.get_column("category").str.strip_chars().eq("").any():
        raise ValueError("category must not be blank")
    if not events.get_column("value").is_finite().all():
        raise ValueError("value must be finite")

    return (
        events.lazy()
        .with_columns(
            pl.col("occurred_at")
            .dt.convert_time_zone("UTC")
            .dt.date()
            .alias("event_date")
        )
        .group_by("event_date", "category")
        .agg(
            pl.len().cast(pl.UInt32).alias("event_count"),
            pl.col("value").sum().alias("total_value"),
        )
        .sort("event_date", "category")
        .select("event_date", "category", "event_count", "total_value")
        .collect()
    )

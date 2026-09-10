from datetime import UTC, datetime

import pytest

pl = pytest.importorskip("polars")

from .solution import daily_category_totals  # noqa: E402


def _events() -> object:
    return pl.DataFrame(
        {
            "occurred_at": [
                datetime(2025, 1, 2, 1, tzinfo=UTC),
                datetime(2025, 1, 1, 23, tzinfo=UTC),
                datetime(2025, 1, 1, 9, tzinfo=UTC),
            ],
            "category": ["beta", "alpha", "beta"],
            "value": [4.0, 2.0, 3.0],
        },
        schema={
            "occurred_at": pl.Datetime("us", "UTC"),
            "category": pl.String,
            "value": pl.Float64,
        },
    )


def test_aggregates_with_lazy_pipeline_and_deterministic_order() -> None:
    events = _events()
    original = events.clone()

    result = daily_category_totals(events)

    assert result.to_dict(as_series=False) == {
        "event_date": [
            datetime(2025, 1, 1).date(),
            datetime(2025, 1, 1).date(),
            datetime(2025, 1, 2).date(),
        ],
        "category": ["alpha", "beta", "beta"],
        "event_count": [1, 1, 1],
        "total_value": [2.0, 3.0, 4.0],
    }
    assert events.equals(original)


@pytest.mark.parametrize("value", [None, float("nan"), float("inf")])
def test_rejects_invalid_values(value: float | None) -> None:
    events = _events().with_columns(
        pl.when(pl.int_range(pl.len()) == 0)
        .then(pl.lit(value))
        .otherwise(pl.col("value"))
        .alias("value")
    )

    with pytest.raises(ValueError):
        daily_category_totals(events)


def test_rejects_wrong_schema_and_blank_categories() -> None:
    with pytest.raises(ValueError, match="typed columns"):
        daily_category_totals(_events().with_columns(pl.col("value").cast(pl.Int64)))
    with pytest.raises(ValueError, match="blank"):
        daily_category_totals(
            _events().with_columns(
                pl.when(pl.int_range(pl.len()) == 0)
                .then(pl.lit(" "))
                .otherwise(pl.col("category"))
                .alias("category")
            )
        )

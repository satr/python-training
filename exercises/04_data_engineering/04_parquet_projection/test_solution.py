from datetime import UTC, datetime, timedelta, timezone
from pathlib import Path

import pytest

pa = pytest.importorskip("pyarrow")

from .solution import (  # noqa: E402
    EVENT_SCHEMA,
    EventRecord,
    build_event_table,
    read_event_window,
    write_event_table,
)


def _records() -> list[EventRecord]:
    return [
        EventRecord("a", datetime(2025, 1, 1, 8, tzinfo=UTC), "view", 1.0),
        EventRecord("b", datetime(2025, 1, 1, 10, tzinfo=UTC), "click", 2.0),
        EventRecord("c", datetime(2025, 1, 1, 12, tzinfo=UTC), "view", 3.0),
    ]


def test_writes_and_reads_projected_half_open_window(tmp_path: Path) -> None:
    path = tmp_path / "events.parquet"
    table = build_event_table(_records())

    assert table.schema.equals(EVENT_SCHEMA)
    write_event_table(table, path)
    result = read_event_window(
        path,
        start=datetime(2025, 1, 1, 10, tzinfo=UTC),
        end=datetime(2025, 1, 1, 12, tzinfo=UTC),
        columns=["event_id", "value"],
    )

    assert result.column_names == ["event_id", "value"]
    assert result.to_pydict() == {"event_id": ["b"], "value": [2.0]}


def test_normalizes_non_utc_bounds_before_filtering(tmp_path: Path) -> None:
    path = tmp_path / "events.parquet"
    write_event_table(build_event_table(_records()), path)
    utc_plus_two = timezone(timedelta(hours=2))

    result = read_event_window(
        path,
        start=datetime(2025, 1, 1, 12, tzinfo=utc_plus_two),
        end=datetime(2025, 1, 1, 14, tzinfo=utc_plus_two),
        columns=["event_id"],
    )

    assert result.to_pydict() == {"event_id": ["b"]}


@pytest.mark.parametrize(
    ("start", "end"),
    [
        (datetime(2025, 1, 1), datetime(2025, 1, 2, tzinfo=UTC)),
        (datetime(2025, 1, 1, tzinfo=UTC), datetime(2025, 1, 2)),
        (
            datetime(2025, 1, 2, tzinfo=UTC),
            datetime(2025, 1, 2, tzinfo=UTC),
        ),
    ],
)
def test_rejects_naive_or_equal_bounds(
    tmp_path: Path, start: datetime, end: datetime
) -> None:
    path = tmp_path / "events.parquet"
    write_event_table(build_event_table(_records()), path)

    with pytest.raises(ValueError):
        read_event_window(path, start=start, end=end, columns=["event_id"])


def test_rejects_genuinely_reversed_bounds(tmp_path: Path) -> None:
    path = tmp_path / "events.parquet"
    write_event_table(build_event_table(_records()), path)

    with pytest.raises(ValueError, match="start must be earlier than end"):
        read_event_window(
            path,
            start=datetime(2025, 1, 2, tzinfo=UTC),
            end=datetime(2025, 1, 1, tzinfo=UTC),
            columns=["event_id"],
        )


@pytest.mark.parametrize(
    ("columns", "message"),
    [
        ([], "columns must be a non-empty sequence"),
        (["event_id", "event_id"], "columns must not contain duplicates"),
    ],
)
def test_rejects_empty_or_duplicate_projections(
    tmp_path: Path, columns: list[str], message: str
) -> None:
    path = tmp_path / "events.parquet"
    write_event_table(build_event_table(_records()), path)

    with pytest.raises(ValueError, match=message):
        read_event_window(
            path,
            start=datetime(2025, 1, 1, tzinfo=UTC),
            end=datetime(2025, 1, 2, tzinfo=UTC),
            columns=columns,
        )


@pytest.mark.parametrize("column_name", ["event_id", "category"])
def test_write_rejects_blank_string_columns(
    tmp_path: Path, column_name: str
) -> None:
    path = tmp_path / "events.parquet"
    values: dict[str, list[object]] = {
        "event_id": ["x"],
        "occurred_at": [datetime(2025, 1, 1, tzinfo=UTC)],
        "category": ["view"],
        "value": [1.0],
    }
    values[column_name] = [" \t"]
    table = pa.Table.from_pydict(values, schema=EVENT_SCHEMA)

    with pytest.raises(
        ValueError, match=rf"{column_name} must not contain blank values"
    ):
        write_event_table(table, path)


def test_rejects_bad_schema_columns_and_records(tmp_path: Path) -> None:
    path = tmp_path / "events.parquet"
    table = build_event_table(_records())
    write_event_table(table, path)

    with pytest.raises(ValueError, match="EVENT_SCHEMA"):
        write_event_table(table.drop(["category"]), path)
    with pytest.raises(ValueError, match="columns"):
        read_event_window(
            path,
            start=datetime(2025, 1, 1, tzinfo=UTC),
            end=datetime(2025, 1, 2, tzinfo=UTC),
            columns=["missing"],
        )
    with pytest.raises(ValueError, match="timezone-aware"):
        build_event_table([EventRecord("x", datetime(2025, 1, 1), "view", 1.0)])
    with pytest.raises(ValueError, match="finite"):
        build_event_table(
            [
                EventRecord(
                    "x",
                    datetime(2025, 1, 1, tzinfo=UTC) + timedelta(hours=1),
                    "view",
                    float("nan"),
                )
            ]
        )

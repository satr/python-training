from __future__ import annotations

import math
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from numbers import Real
from pathlib import Path

import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

EVENT_SCHEMA = pa.schema(
    [
        pa.field("event_id", pa.string(), nullable=False),
        pa.field("occurred_at", pa.timestamp("us", tz="UTC"), nullable=False),
        pa.field("category", pa.string(), nullable=False),
        pa.field("value", pa.float64(), nullable=False),
    ]
)


@dataclass(frozen=True, slots=True)
class EventRecord:
    event_id: str
    occurred_at: datetime
    category: str
    value: float


def build_event_table(events: Iterable[EventRecord]) -> pa.Table:
    records = list(events)
    for event in records:
        if not isinstance(event, EventRecord):
            raise TypeError("events must contain EventRecord values")
        if not isinstance(event.event_id, str) or not isinstance(event.category, str):
            raise ValueError("event_id and category must be strings")
        if not event.event_id.strip() or not event.category.strip():
            raise ValueError("event_id and category must not be blank")
        if not isinstance(event.occurred_at, datetime):
            raise ValueError("occurred_at must be a datetime")
        if event.occurred_at.tzinfo is None or event.occurred_at.utcoffset() is None:
            raise ValueError("occurred_at must be timezone-aware")
        if (
            isinstance(event.value, bool)
            or not isinstance(event.value, Real)
            or not math.isfinite(event.value)
        ):
            raise ValueError("value must be finite")

    return pa.Table.from_arrays(
        [
            pa.array((event.event_id for event in records), type=pa.string()),
            pa.array(
                (event.occurred_at.astimezone(UTC) for event in records),
                type=pa.timestamp("us", tz="UTC"),
            ),
            pa.array((event.category for event in records), type=pa.string()),
            pa.array((event.value for event in records), type=pa.float64()),
        ],
        schema=EVENT_SCHEMA,
    )


def write_event_table(table: pa.Table, path: str | Path) -> None:
    if not isinstance(table, pa.Table):
        raise TypeError("table must be an Arrow Table")
    if not table.schema.equals(EVENT_SCHEMA):
        raise ValueError("table does not match EVENT_SCHEMA")
    table.validate(full=True)
    if any(column.null_count for column in table.columns):
        raise ValueError("table must not contain null values")
    for column_name in ("event_id", "category"):
        if any(not value.strip() for value in table[column_name].to_pylist()):
            raise ValueError(f"{column_name} must not contain blank values")
    if table.num_rows and not pc.all(pc.is_finite(table["value"])).as_py():
        raise ValueError("value must be finite")
    pq.write_table(table, Path(path))


def read_event_window(
    path: str | Path,
    *,
    start: datetime,
    end: datetime,
    columns: Sequence[str],
) -> pa.Table:
    if start.tzinfo is None or start.utcoffset() is None:
        raise ValueError("start must be timezone-aware")
    if end.tzinfo is None or end.utcoffset() is None:
        raise ValueError("end must be timezone-aware")
    start_utc = start.astimezone(UTC)
    end_utc = end.astimezone(UTC)
    if start_utc >= end_utc:
        raise ValueError("start must be earlier than end")
    if isinstance(columns, str) or not columns:
        raise ValueError("columns must be a non-empty sequence")
    selected = list(columns)
    if len(selected) != len(set(selected)):
        raise ValueError("columns must not contain duplicates")
    unknown = set(selected) - set(EVENT_SCHEMA.names)
    if unknown:
        raise ValueError("columns must be present in EVENT_SCHEMA")

    parquet_file = pq.ParquetFile(Path(path))
    if not parquet_file.schema_arrow.equals(EVENT_SCHEMA):
        raise ValueError("Parquet file does not match EVENT_SCHEMA")
    return pq.read_table(
        Path(path),
        columns=selected,
        filters=[
            ("occurred_at", ">=", start_utc),
            ("occurred_at", "<", end_utc),
        ],
    )

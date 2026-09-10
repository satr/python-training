from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import pyarrow as pa

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
    raise NotImplementedError


def write_event_table(table: pa.Table, path: str | Path) -> None:
    raise NotImplementedError


def read_event_window(
    path: str | Path,
    *,
    start: datetime,
    end: datetime,
    columns: Sequence[str],
) -> pa.Table:
    raise NotImplementedError

from __future__ import annotations

import math
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(frozen=True, slots=True)
class Event:
    event_id: str
    occurred_at: datetime
    value: float


def normalize_events(rows: Iterable[Mapping[str, object]]) -> list[Event]:
    deduplicated: dict[str, Event] = {}
    for row in rows:
        try:
            event_id = str(row["event_id"]).strip()
            timestamp = str(row["occurred_at"])
            raw_value = row["value"]
            if not isinstance(raw_value, (str, int, float)):
                raise TypeError
            value = float(raw_value)
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(
                "event requires event_id, occurred_at, and value"
            ) from error
        if not event_id or not math.isfinite(value):
            raise ValueError("event_id must be non-empty and value must be finite")
        try:
            occurred_at = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        except ValueError as error:
            raise ValueError(f"invalid timestamp for event {event_id}") from error
        if occurred_at.tzinfo is None:
            raise ValueError(f"timestamp must include a timezone for event {event_id}")
        deduplicated[event_id] = Event(event_id, occurred_at.astimezone(UTC), value)
    return sorted(deduplicated.values(), key=lambda event: event.occurred_at)

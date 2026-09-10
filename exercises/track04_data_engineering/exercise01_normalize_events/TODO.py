from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Event:
    event_id: str
    occurred_at: datetime
    value: float


def normalize_events(rows: Iterable[Mapping[str, object]]) -> list[Event]:
    raise NotImplementedError


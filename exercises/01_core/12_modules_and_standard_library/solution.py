from __future__ import annotations

from datetime import date, timedelta


def parse_deadline(value: str) -> date:
    return date.fromisoformat(value)


def next_business_day(day: date) -> date:
    candidate = day + timedelta(days=1)
    while candidate.weekday() >= 5:
        candidate += timedelta(days=1)
    return candidate

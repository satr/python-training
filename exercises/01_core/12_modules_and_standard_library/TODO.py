from __future__ import annotations

from datetime import date


def parse_deadline(value: str) -> date:
    raise NotImplementedError


def next_business_day(day: date) -> date:
    raise NotImplementedError

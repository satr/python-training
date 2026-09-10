from datetime import date

import pytest

from .solution import next_business_day, parse_deadline


def test_parse_deadline_reads_iso_date() -> None:
    assert parse_deadline("2026-09-10") == date(2026, 9, 10)


@pytest.mark.parametrize("value", ["10/09/2026", "not-a-date", "2026-02-30"])
def test_parse_deadline_rejects_invalid_dates(value: str) -> None:
    with pytest.raises(ValueError):
        parse_deadline(value)


@pytest.mark.parametrize(
    ("day", "expected"),
    [
        (date(2026, 9, 9), date(2026, 9, 10)),
        (date(2026, 9, 11), date(2026, 9, 14)),
        (date(2026, 9, 12), date(2026, 9, 14)),
        (date(2026, 9, 13), date(2026, 9, 14)),
    ],
)
def test_next_business_day_is_strictly_later_and_skips_weekends(
    day: date, expected: date
) -> None:
    assert next_business_day(day) == expected

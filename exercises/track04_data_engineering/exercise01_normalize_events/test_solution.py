from datetime import UTC, datetime

import pytest

from .solution import Event, normalize_events


def test_normalizes_deduplicates_and_sorts() -> None:
    rows = [
        {"event_id": "b", "occurred_at": "2025-01-01T12:00:00+02:00", "value": "2"},
        {"event_id": "a", "occurred_at": "2025-01-01T09:00:00Z", "value": 1},
        {"event_id": "a", "occurred_at": "2025-01-01T11:00:00Z", "value": 3},
    ]
    assert normalize_events(rows) == [
        Event("b", datetime(2025, 1, 1, 10, tzinfo=UTC), 2.0),
        Event("a", datetime(2025, 1, 1, 11, tzinfo=UTC), 3.0),
    ]


@pytest.mark.parametrize(
    "row",
    [
        {},
        {"event_id": "", "occurred_at": "2025-01-01T00:00:00Z", "value": 1},
        {"event_id": "a", "occurred_at": "2025-01-01", "value": 1},
        {"event_id": "a", "occurred_at": "bad", "value": 1},
    ],
)
def test_rejects_bad_rows(row: dict[str, object]) -> None:
    with pytest.raises(ValueError):
        normalize_events([row])

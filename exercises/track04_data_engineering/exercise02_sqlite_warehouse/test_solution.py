import sqlite3
from contextlib import suppress
from datetime import UTC, datetime

from .solution import create_schema, daily_totals, load_events


def test_load_is_idempotent_and_aggregates_by_day() -> None:
    connection = sqlite3.connect(":memory:")
    create_schema(connection)
    events = [
        ("a", datetime(2025, 1, 1, 10, tzinfo=UTC), 2.0),
        ("b", datetime(2025, 1, 1, 11, tzinfo=UTC), 3.0),
        ("c", datetime(2025, 1, 2, 9, tzinfo=UTC), 4.0),
    ]
    load_events(connection, events)
    load_events(connection, [("a", events[0][1], 5.0)])
    assert daily_totals(connection) == [("2025-01-01", 8.0), ("2025-01-02", 4.0)]
    assert connection.execute("SELECT COUNT(*) FROM events").fetchone() == (3,)


def test_batch_rolls_back_on_error() -> None:
    connection = sqlite3.connect(":memory:")
    create_schema(connection)
    with suppress(sqlite3.IntegrityError):
        load_events(
            connection,
            [
                ("valid", datetime.now(UTC), 1.0),
                (None, datetime.now(UTC), 2.0),  # type: ignore[list-item]
            ],
        )
    assert connection.execute("SELECT COUNT(*) FROM events").fetchone() == (0,)

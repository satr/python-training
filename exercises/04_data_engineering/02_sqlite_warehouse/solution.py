from __future__ import annotations

import sqlite3
from collections.abc import Iterable
from datetime import datetime


def create_schema(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS events (
            event_id TEXT PRIMARY KEY NOT NULL,
            occurred_at TEXT NOT NULL,
            value REAL NOT NULL
        )
        """
    )


def load_events(
    connection: sqlite3.Connection,
    events: Iterable[tuple[str, datetime, float]],
) -> None:
    with connection:
        connection.executemany(
            """
            INSERT INTO events(event_id, occurred_at, value)
            VALUES (?, ?, ?)
            ON CONFLICT(event_id) DO UPDATE SET
                occurred_at = excluded.occurred_at,
                value = excluded.value
            """,
            (
                (event_id, occurred_at.isoformat(), value)
                for event_id, occurred_at, value in events
            ),
        )


def daily_totals(connection: sqlite3.Connection) -> list[tuple[str, float]]:
    rows = connection.execute(
        """
        SELECT substr(occurred_at, 1, 10) AS event_date, SUM(value)
        FROM events
        GROUP BY event_date
        ORDER BY event_date
        """
    )
    return [(str(event_date), float(total)) for event_date, total in rows]

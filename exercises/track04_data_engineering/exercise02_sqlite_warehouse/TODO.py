from __future__ import annotations

import sqlite3
from collections.abc import Iterable
from datetime import datetime


def create_schema(connection: sqlite3.Connection) -> None:
    raise NotImplementedError


def load_events(
    connection: sqlite3.Connection,
    events: Iterable[tuple[str, datetime, float]],
) -> None:
    raise NotImplementedError


def daily_totals(connection: sqlite3.Connection) -> list[tuple[str, float]]:
    raise NotImplementedError


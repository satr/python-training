from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path


def load_tasks(path: Path) -> list[str]:
    raise NotImplementedError


def save_tasks(path: Path, tasks: Iterable[str]) -> int:
    raise NotImplementedError

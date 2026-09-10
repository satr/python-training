from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path


def load_tasks(path: Path) -> list[str]:
    with path.open(encoding="utf-8") as task_file:
        lines = (line.strip() for line in task_file)
        return [line for line in lines if line and not line.startswith("#")]


def save_tasks(path: Path, tasks: Iterable[str]) -> int:
    count = 0
    with path.open("w", encoding="utf-8", newline="\n") as task_file:
        for task in tasks:
            task_file.write(f"{task}\n")
            count += 1
    return count

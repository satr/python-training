from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Task:
    title: str
    completed: bool = False


class TaskList:
    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, title: str) -> Task:
        raise NotImplementedError

    def complete(self, title: str) -> bool:
        raise NotImplementedError

    def pending(self) -> list[str]:
        raise NotImplementedError

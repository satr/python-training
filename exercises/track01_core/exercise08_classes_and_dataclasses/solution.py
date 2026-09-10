from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Task:
    title: str
    completed: bool = False


class TaskList:
    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add(self, title: str) -> Task:
        normalized_title = title.strip()
        if not normalized_title:
            raise ValueError("title must not be blank")
        if any(task.title == normalized_title for task in self._tasks):
            raise ValueError("task title must be unique")

        task = Task(normalized_title)
        self._tasks.append(task)
        return task

    def complete(self, title: str) -> bool:
        normalized_title = title.strip()
        for task in self._tasks:
            if task.title == normalized_title:
                task.completed = True
                return True
        return False

    def pending(self) -> list[str]:
        return [task.title for task in self._tasks if not task.completed]

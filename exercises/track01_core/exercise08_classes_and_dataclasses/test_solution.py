import pytest

from .solution import Task, TaskList


def test_task_defaults_to_incomplete() -> None:
    assert Task("write tests") == Task("write tests", completed=False)


def test_task_list_adds_completes_and_preserves_insertion_order() -> None:
    tasks = TaskList()
    added = tasks.add("  write tests  ")
    tasks.add("review code")

    assert added == Task("write tests")
    assert tasks.complete("write tests") is True
    assert tasks.complete("missing") is False
    assert tasks.pending() == ["review code"]


@pytest.mark.parametrize("title", ["", " ", "\t"])
def test_task_list_rejects_blank_titles(title: str) -> None:
    with pytest.raises(ValueError, match="blank"):
        TaskList().add(title)


def test_task_list_rejects_duplicate_titles() -> None:
    tasks = TaskList()
    tasks.add("write tests")
    with pytest.raises(ValueError, match="unique"):
        tasks.add(" write tests ")


def test_task_list_instances_are_independent() -> None:
    first = TaskList()
    second = TaskList()
    first.add("first task")
    assert second.pending() == []

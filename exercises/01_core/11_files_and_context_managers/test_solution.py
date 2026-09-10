from pathlib import Path

from .solution import load_tasks, save_tasks


def test_load_tasks_strips_lines_and_ignores_blanks_and_comments(
    tmp_path: Path,
) -> None:
    path = tmp_path / "tasks.txt"
    path.write_text("  buy café beans  \n\n # later\nwrite tests\n", encoding="utf-8")
    assert load_tasks(path) == ["buy café beans", "write tests"]


def test_save_tasks_overwrites_deterministically_and_returns_count(
    tmp_path: Path,
) -> None:
    path = tmp_path / "tasks.txt"
    path.write_text("old task\n", encoding="utf-8")
    tasks = (task for task in ["buy café beans", "write tests"])

    assert save_tasks(path, tasks) == 2
    assert path.read_bytes() == "buy café beans\nwrite tests\n".encode()


def test_save_tasks_handles_empty_iterable(tmp_path: Path) -> None:
    path = tmp_path / "tasks.txt"
    path.write_text("old task\n", encoding="utf-8")
    assert save_tasks(path, []) == 0
    assert path.read_text(encoding="utf-8") == ""

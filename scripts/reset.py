from __future__ import annotations

import argparse
import contextlib
import os
import re
import shutil
import stat
from collections.abc import Iterator
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXERCISES = ROOT / "exercises"
TRACK_PATTERN = re.compile(r"\d{2}_[a-z0-9_]+")
EXERCISE_PATTERN = re.compile(r"\d{2}_[a-z0-9_]+")


def exercise_directories() -> list[Path]:
    return sorted(
        path.parent
        for path in EXERCISES.glob("[0-9][0-9]_*/[0-9][0-9]_*/TODO.py")
        if not path.parent.is_symlink()
    )


def resolve_exercise(exercise: Path) -> Path:
    """Resolve and validate an exercise directory inside the exercises root."""
    try:
        resolved = exercise.resolve(strict=True)
    except OSError as error:
        raise SystemExit(f"Not an exercise directory: {exercise}") from error

    try:
        relative = resolved.relative_to(EXERCISES.resolve(strict=True))
    except ValueError as error:
        raise SystemExit(f"Not an exercise directory: {exercise}") from error
    if (
        len(relative.parts) != 2
        or not TRACK_PATTERN.fullmatch(relative.parts[0])
        or not EXERCISE_PATTERN.fullmatch(relative.parts[1])
        or not resolved.is_dir()
    ):
        raise SystemExit(f"Not an exercise directory: {exercise}")

    # Do not accept an exercise reached through a symlink, even if its target
    # happens to be inside the repository.
    current = EXERCISES
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            raise SystemExit(f"Not an exercise directory: {exercise}")
    return resolved


def reset(exercise: Path) -> None:
    exercise = resolve_exercise(exercise)
    relative = exercise.relative_to(EXERCISES.resolve(strict=True))
    try:
        with open_exercise_directory(relative) as directory_fd:
            source_fd = os.open(
                "TODO.py",
                os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW,
                dir_fd=directory_fd,
            )
            with os.fdopen(source_fd, "rb") as source_file:
                if not stat.S_ISREG(os.fstat(source_file.fileno()).st_mode):
                    raise OSError("TODO.py is not a regular file")
                destination_fd = os.open(
                    "solution.py",
                    os.O_WRONLY | os.O_NONBLOCK | os.O_NOFOLLOW,
                    dir_fd=directory_fd,
                )
                with os.fdopen(destination_fd, "wb") as destination_file:
                    if not stat.S_ISREG(
                        os.fstat(destination_file.fileno()).st_mode
                    ):
                        raise OSError("solution.py is not a regular file")
                    os.ftruncate(destination_file.fileno(), 0)
                    shutil.copyfileobj(source_file, destination_file)
    except OSError as error:
        raise SystemExit(f"Not an exercise directory: {exercise}") from error
    print(f"Reset {exercise.relative_to(ROOT)}")


@contextlib.contextmanager
def open_exercise_directory(relative: Path) -> Iterator[int]:
    """Open an exercise using stable, symlink-free directory descriptors."""
    directory_fd = os.open(
        EXERCISES, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    )
    try:
        for part in relative.parts:
            child_fd = os.open(
                part,
                os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                dir_fd=directory_fd,
            )
            os.close(directory_fd)
            directory_fd = child_fd
        yield directory_fd
    finally:
        os.close(directory_fd)


def main() -> None:
    parser = argparse.ArgumentParser(description="Reset active exercise solutions")
    parser.add_argument("exercise", nargs="?", type=Path)
    parser.add_argument(
        "--from-env",
        action="store_true",
        help="read the exercise directory from EXERCISE",
    )
    parser.add_argument("--all", action="store_true", dest="reset_all")
    args = parser.parse_args()

    if args.reset_all:
        answer = input("Overwrite every solution.py with TODO.py? [y/N] ")
        if answer.lower() != "y":
            print("Cancelled")
            return
        for directory in exercise_directories():
            reset(directory)
        return

    if args.from_env:
        if args.exercise is not None:
            parser.error("--from-env cannot be combined with an exercise directory")
        value = os.environ.get("EXERCISE")
        if not value:
            parser.error("EXERCISE is not set")
        directory = Path(value)
    elif args.exercise is None:
        parser.error("provide an exercise directory or --all")
    else:
        directory = args.exercise
    if not directory.is_absolute():
        directory = ROOT / directory
    reset(directory)


if __name__ == "__main__":
    main()

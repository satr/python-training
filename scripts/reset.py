from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXERCISES = ROOT / "exercises"


def exercise_directories() -> list[Path]:
    return sorted(
        path.parent for path in EXERCISES.glob("track[0-9][0-9]_*/exercise*/TODO.py")
    )


def reset(exercise: Path) -> None:
    source = exercise / "TODO.py"
    destination = exercise / "solution.py"
    if not source.is_file() or not destination.is_file():
        raise SystemExit(f"Not an exercise directory: {exercise}")
    shutil.copyfile(source, destination)
    print(f"Reset {exercise.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Reset active exercise solutions")
    parser.add_argument("exercise", nargs="?", type=Path)
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

    if args.exercise is None:
        parser.error("provide an exercise directory or --all")
    directory = args.exercise
    if not directory.is_absolute():
        directory = ROOT / directory
    reset(directory.resolve())


if __name__ == "__main__":
    main()

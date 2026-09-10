from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXERCISES = ROOT / "exercises"
REQUIRED = {"README.md", "TODO.py", "__init__.py", "solution.py", "test_solution.py"}
TRACK_PATTERN = re.compile(r"\d{2}_[a-z0-9_]+")
EXERCISE_PATTERN = re.compile(r"\d{2}_[a-z0-9_]+")


def main() -> None:
    errors: list[str] = []
    for track in sorted(path for path in EXERCISES.iterdir() if path.is_dir()):
        if track.name == "__pycache__":
            continue
        if not TRACK_PATTERN.fullmatch(track.name):
            errors.append(f"Invalid track name: {track.relative_to(ROOT)}")
            continue
        exercise_numbers: list[int] = []
        for exercise in sorted(path for path in track.iterdir() if path.is_dir()):
            if exercise.name == "__pycache__":
                continue
            if not EXERCISE_PATTERN.fullmatch(exercise.name):
                errors.append(f"Invalid exercise name: {exercise.relative_to(ROOT)}")
                continue
            exercise_numbers.append(int(exercise.name[:2]))
            missing = REQUIRED - {path.name for path in exercise.iterdir()}
            if missing:
                errors.append(
                    f"{exercise.relative_to(ROOT)} missing {', '.join(sorted(missing))}"
                )
        expected = list(range(1, len(exercise_numbers) + 1))
        if exercise_numbers != expected:
            errors.append(
                f"{track.name} numbering is {exercise_numbers}, expected {expected}"
            )

    if errors:
        raise SystemExit("\n".join(errors))
    print("Exercise layout is valid")


if __name__ == "__main__":
    main()

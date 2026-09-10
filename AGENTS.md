# Training and repository instructions

## Purpose

This is a practical Python curriculum for learning by implementation. It
progresses from the language itself through concurrent programs, production
software practices, data pipelines, and AI-enabled applications.

## Teaching workflow

1. Explain the relevant idea briefly before changing code.
2. Let the learner attempt the task in `solution.py`.
3. Prefer hints and review over immediately supplying the final answer.
4. Run the focused exercise target after each change.
5. Record meaningful learning progress in the progress log below.

## Exercise contract

Exercises live at `exercises/trackNN_name/exerciseNN_name/`. These prefixes
preserve learning order while remaining valid Python package names. Each
directory must contain:

- `README.md` with `Theory`, `Task`, `Run`, and `Further practice` sections.
- `solution.py` containing the active implementation.
- `TODO.py` containing matching signatures and `NotImplementedError` stubs.
- `test_solution.py` containing deterministic, behavior-focused pytest tests.
- `__init__.py`.

Number exercises from `01` inside each track. Keep imports side-effect free.
Do not hide a final implementation in an exercise README. Standard exercises
must not require network access, credentials, paid APIs, or large downloads.
Mark external-service tests with `pytest.mark.integration`.

When adding an exercise:

1. Add it to `exercises/README.md`.
2. Ensure `python scripts/verify_layout.py` accepts it.
3. Run its tests, Ruff, and mypy.
4. Preserve `TODO.py` as a resettable template.

## Repository commands

- `make exercise EXERCISE=<directory>` - run one exercise.
- `make test` - run all non-integration tests.
- `make lint` - run Ruff.
- `make typecheck` - run mypy.
- `make check` - run layout, lint, type checking, and tests.
- `make reset EXERCISE=<directory>` - reset one active solution.
- `make reset-all` - reset every active solution after confirmation.

## Progress log

- 2026-09-10: Repository foundation and five-track curriculum created.
- 2026-09-10: Added vendor-neutral Copilot agents with iterative planning,
  implementation, verification, validation, and security gates.
- Next: complete the core track in order, beginning with measurements.

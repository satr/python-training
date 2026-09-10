# Training and repository instructions

## Purpose

This is a practical Python curriculum for learning by implementation. It
progresses from the language itself through concurrent programs, production
software practices, data pipelines, and AI-enabled applications.

## Teaching workflow

1. Explain the relevant idea briefly with a small concrete example before asking
   the learner to change code.
2. Let the learner attempt the task in `solution.py` after reading the
   exercise's `Learn before coding` section.
3. Prefer hints and review over immediately supplying the final answer.
4. Run the focused, dedicated exercise target after each change.
5. Record meaningful learning progress in the progress log below.

## Exercise contract

Exercises live at `exercises/trackNN_name/exerciseNN_name/`. These prefixes
preserve learning order while remaining valid Python package names. Each
directory must contain:

- `README.md` with `Theory`, `Task`, `Run`, and `Further practice` sections.
  It must also include a `Learn before coding` section immediately before
  `Task`, with exercise-specific preparation grounded in the implementation
  and tests but without revealing the final implementation. Keep ordinary
  explanation as prose or simple bullets. Where guidance or a requirement
  contains distinct actions, decisions, edge cases, or ordered steps, use a
  concise parent bullet with indented nested bullets; do not mechanically turn
  every paragraph or `Task` into nested bullets. Keep preparation immediately
  before `Task`. Put substantial executable examples in language-tagged fenced
  code blocks; keep short identifiers, literals, operators, and API names inline
  when they are merely being referenced.
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

- `make <track>_<number>_<exercise>` - run one exercise (use `make help` for
  the complete target list).
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
- 2026-09-10: Expanded Core Python into a concept-first, 14-exercise beginner
  curriculum.
- 2026-09-10: Added optional arguments, a testable argparse exercise, and
  configuration precedence with typed validation.
- 2026-09-10: Added Polars and Parquet data pipelines plus NumPy scaling and a
  deterministic CPU-only PyTorch classifier.
- Next: continue the concurrency and async track.

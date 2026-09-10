# Python Training

An exercise-driven path from Python fundamentals to production-oriented data
engineering and AI applications.

The repository is designed for deliberate practice: read a short explanation,
implement a focused task, run its tests, and compare your approach with the
working version. Start with the [exercise index](exercises/README.md).

## Learning workflow

Every exercise contains:

- `README.md` - theory, task, and the exact command to run.
- `solution.py` - the active, working implementation.
- `TODO.py` - an untouched practice copy with the same public API.
- `test_solution.py` - behavior-focused tests.

To practise an exercise, replace `solution.py` with its `TODO.py` template:

```bash
make reset EXERCISE=exercises/track01_core/exercise01_values_and_strings
```

Then implement the missing behavior and run:

```bash
make exercise EXERCISE=exercises/track01_core/exercise01_values_and_strings
```

`make reset-all` resets every exercise and requires explicit confirmation.

## Curriculum

| Track | Focus |
| --- | --- |
| [01 Core Python](exercises/track01_core) | Types, control flow, functions, collections, errors, iterators, OOP, typing |
| [02 Concurrency and async](exercises/track02_concurrency_async) | Threads, processes, asyncio, queues, cancellation |
| [03 Software engineering](exercises/track03_software_engineering) | Testing, architecture, APIs, configuration, observability |
| [04 Data engineering](exercises/track04_data_engineering) | Files, SQL, ETL, validation, pipelines, orchestration concepts |
| [05 AI applications](exercises/track05_ai_applications) | ML foundations, embeddings, retrieval, evaluation, production patterns |

The core track provides a complete beginner sequence, while the other tracks
start with representative exercises. The
[roadmap](exercises/README.md#roadmap) shows how the course can grow without
losing its progression.

## Quick start

Python 3.11 or newer is required.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
make check
```

See [INSTALL.md](INSTALL.md) for platform notes and [AGENTS.md](AGENTS.md) for
the exercise-authoring and AI-assistant workflow.

## AI agent workflow

Vendor-neutral GitHub Copilot custom agents live in
[`.github/agents`](.github/agents). The profiles omit the `model` property so
they inherit the model selected by the supported Copilot environment rather
than depending on a specific AI vendor or model.

Select `orchestrator` for repository changes. It delegates to dedicated
planning, implementation, behavior verification, repository validation, and
security subagents. Failed gates return to implementation and repeat until all
checks pass or a concrete blocker is reported. Every role must redact
credentials, tokens, personal data, private endpoints, and other sensitive
information from prompts, logs, handoffs, patches, and reports.

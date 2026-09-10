.PHONY: help install test lint format typecheck layout check exercise reset reset-all

PYTHON ?= python

help:
	@printf '%s\n' \
	  'install                  Install development dependencies' \
	  'test                     Run all fast tests' \
	  'check                    Run layout, lint, types, and tests' \
	  'exercise EXERCISE=<dir>  Test one exercise' \
	  'reset EXERCISE=<dir>     Restore one solution from TODO.py' \
	  'reset-all                Restore every solution (destructive)'

install:
	$(PYTHON) -m pip install -e ".[dev]"

test:
	$(PYTHON) -m pytest -m "not integration"

lint:
	$(PYTHON) -m ruff check .

format:
	$(PYTHON) -m ruff format .

typecheck:
	$(PYTHON) -m mypy exercises scripts

layout:
	$(PYTHON) scripts/verify_layout.py

check: layout lint typecheck test

exercise:
	@test -n "$(EXERCISE)" || (echo "Set EXERCISE=<exercise-directory>" && exit 2)
	$(PYTHON) -m pytest "$(EXERCISE)/test_solution.py"

reset:
	@test -n "$(EXERCISE)" || (echo "Set EXERCISE=<exercise-directory>" && exit 2)
	$(PYTHON) scripts/reset.py "$(EXERCISE)"

reset-all:
	$(PYTHON) scripts/reset.py --all


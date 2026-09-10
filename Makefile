.PHONY: help install test lint format typecheck layout check reset reset-all \
	01_core_01_values_and_strings 01_core_02_conditionals_and_booleans \
	01_core_03_loops_and_ranges 01_core_04_functions_and_parameters \
	01_core_05_lists_and_tuples 01_core_06_dictionaries_and_sets \
	01_core_07_comprehensions 01_core_08_classes_and_dataclasses \
	01_core_09_exceptions_and_validation 01_core_10_iterators_and_generators \
	01_core_11_files_and_context_managers 01_core_12_modules_and_standard_library \
	01_core_13_decorators_and_closures 01_core_14_typing_and_protocols \
	01_core_15_command_line_arguments \
	02_concurrency_01_bounded_map 02_concurrency_02_async_pipeline \
	03_software_engineering_01_configuration 03_software_engineering_02_order_service \
	03_software_engineering_03_configuration_precedence \
	04_data_engineering_01_normalize_events 04_data_engineering_02_sqlite_warehouse \
	04_data_engineering_03_polars_lazy_aggregations \
	04_data_engineering_04_parquet_projection \
	05_ai_applications_01_vector_search 05_ai_applications_02_retrieval_evaluation \
	05_ai_applications_03_numpy_feature_scaling \
	05_ai_applications_04_pytorch_binary_classifier

PYTHON ?= $(if $(filter Windows_NT,$(OS)),$(if $(wildcard .venv/Scripts/python.exe),.venv/Scripts/python.exe,python),$(if $(wildcard .venv/bin/python),.venv/bin/python,python3))
export EXERCISE

help:
	@printf '%s\n' \
	  'install                  Install development dependencies' \
	  'test                     Run all fast tests' \
	  'check                    Run layout, lint, types, and tests' \
	  '01_core_01_values_and_strings  Test Values and strings' \
	  '01_core_02_conditionals_and_booleans  Test Conditionals and booleans' \
	  '01_core_03_loops_and_ranges  Test Loops and ranges' \
	  '01_core_04_functions_and_parameters  Test Functions and parameters' \
	  '01_core_05_lists_and_tuples  Test Lists and tuples' \
	  '01_core_06_dictionaries_and_sets  Test Dictionaries and sets' \
	  '01_core_07_comprehensions  Test Comprehensions' \
	  '01_core_08_classes_and_dataclasses  Test Classes and dataclasses' \
	  '01_core_09_exceptions_and_validation  Test Exceptions and validation' \
	  '01_core_10_iterators_and_generators  Test Iterators and generators' \
	  '01_core_11_files_and_context_managers  Test Files and context managers' \
	  '01_core_12_modules_and_standard_library  Test Modules and standard library' \
	  '01_core_13_decorators_and_closures  Test Decorators and closures' \
	  '01_core_14_typing_and_protocols  Test Typing and protocols' \
	  '01_core_15_command_line_arguments  Test Command-line arguments' \
	  '02_concurrency_01_bounded_map  Test Bounded map' \
	  '02_concurrency_02_async_pipeline  Test Async pipeline' \
	  '03_software_engineering_01_configuration  Test Configuration' \
	  '03_software_engineering_02_order_service  Test Order service' \
	  '03_software_engineering_03_configuration_precedence  Test Configuration precedence' \
	  '04_data_engineering_01_normalize_events  Test Normalize events' \
	  '04_data_engineering_02_sqlite_warehouse  Test SQLite warehouse' \
	  '04_data_engineering_03_polars_lazy_aggregations  Test Polars lazy aggregations' \
	  '04_data_engineering_04_parquet_projection  Test Parquet projection' \
	  '05_ai_applications_01_vector_search  Test Vector search' \
	  '05_ai_applications_02_retrieval_evaluation  Test Retrieval evaluation' \
	  '05_ai_applications_03_numpy_feature_scaling  Test NumPy feature scaling' \
	  '05_ai_applications_04_pytorch_binary_classifier  Test PyTorch binary classifier' \
	  'reset EXERCISE=<dir>     Restore one solution from TODO.py' \
	  'reset-all                Restore every solution (destructive)'

install:
	"$(PYTHON)" -m pip install -e ".[dev,data,ai,pytorch]"

test:
	"$(PYTHON)" -m pytest --import-mode=importlib -m "not integration"

lint:
	"$(PYTHON)" -m ruff check .

format:
	"$(PYTHON)" -m ruff format .

typecheck:
	find exercises scripts -type f -name '*.py' ! -name 'TODO.py' ! -name 'test_solution.py' -exec sh -c \
		'for file do \
			dir=$$(dirname "$$file"); module=$$(basename "$$file" .py); \
			MYPYPATH="$$dir" "$(PYTHON)" -m mypy --module "$$module" || exit; \
		done' sh {} +

layout:
	"$(PYTHON)" scripts/verify_layout.py

check: layout lint typecheck test

01_core_01_values_and_strings:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/01_values_and_strings/test_solution.py

01_core_02_conditionals_and_booleans:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/02_conditionals_and_booleans/test_solution.py

01_core_03_loops_and_ranges:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/03_loops_and_ranges/test_solution.py

01_core_04_functions_and_parameters:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/04_functions_and_parameters/test_solution.py

01_core_05_lists_and_tuples:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/05_lists_and_tuples/test_solution.py

01_core_06_dictionaries_and_sets:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/06_dictionaries_and_sets/test_solution.py

01_core_07_comprehensions:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/07_comprehensions/test_solution.py

01_core_08_classes_and_dataclasses:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/08_classes_and_dataclasses/test_solution.py

01_core_09_exceptions_and_validation:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/09_exceptions_and_validation/test_solution.py

01_core_10_iterators_and_generators:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/10_iterators_and_generators/test_solution.py

01_core_11_files_and_context_managers:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/11_files_and_context_managers/test_solution.py

01_core_12_modules_and_standard_library:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/12_modules_and_standard_library/test_solution.py

01_core_13_decorators_and_closures:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/13_decorators_and_closures/test_solution.py

01_core_14_typing_and_protocols:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/14_typing_and_protocols/test_solution.py

01_core_15_command_line_arguments:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/01_core/15_command_line_arguments/test_solution.py

02_concurrency_01_bounded_map:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/02_concurrency_async/01_bounded_map/test_solution.py

02_concurrency_02_async_pipeline:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/02_concurrency_async/02_async_pipeline/test_solution.py

03_software_engineering_01_configuration:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/03_software_engineering/01_configuration/test_solution.py

03_software_engineering_02_order_service:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/03_software_engineering/02_order_service/test_solution.py

03_software_engineering_03_configuration_precedence:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/03_software_engineering/03_configuration_precedence/test_solution.py

04_data_engineering_01_normalize_events:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/04_data_engineering/01_normalize_events/test_solution.py

04_data_engineering_02_sqlite_warehouse:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/04_data_engineering/02_sqlite_warehouse/test_solution.py

04_data_engineering_03_polars_lazy_aggregations:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/04_data_engineering/03_polars_lazy_aggregations/test_solution.py

04_data_engineering_04_parquet_projection:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/04_data_engineering/04_parquet_projection/test_solution.py

05_ai_applications_01_vector_search:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/05_ai_applications/01_vector_search/test_solution.py

05_ai_applications_02_retrieval_evaluation:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/05_ai_applications/02_retrieval_evaluation/test_solution.py

05_ai_applications_03_numpy_feature_scaling:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/05_ai_applications/03_numpy_feature_scaling/test_solution.py

05_ai_applications_04_pytorch_binary_classifier:
	"$(PYTHON)" -m pytest --import-mode=importlib exercises/05_ai_applications/04_pytorch_binary_classifier/test_solution.py

reset:
	$(if $(EXERCISE),,$(error Set EXERCISE=<exercise-directory>))
	"$(PYTHON)" scripts/reset.py --from-env

reset-all:
	"$(PYTHON)" scripts/reset.py --all

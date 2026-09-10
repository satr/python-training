# Exercise index

Work through the tracks in order. Within each track, exercise numbers restart
at `01`.

## 01 Core Python

1. [Values and strings](01_core/01_values_and_strings) -
   arithmetic, variables, f-strings, and numeric formatting.
2. [Conditionals and booleans](01_core/02_conditionals_and_booleans) -
   boolean expressions, branches, and threshold rules.
3. [Loops and ranges](01_core/03_loops_and_ranges) - repetition,
   state updates, ranges, and list building.
4. [Functions and parameters](01_core/04_functions_and_parameters) -
   composition, defaults, keyword-only parameters, and validation.
5. [Lists and tuples](01_core/05_lists_and_tuples) - collection
   summaries, sorting, slicing, and immutable result groups.
6. [Dictionaries and sets](01_core/06_dictionaries_and_sets) -
   counting, lookup, intersections, and deterministic ordering.
7. [Comprehensions](01_core/07_comprehensions) - concise
   transformations and filters that create new collections.
8. [Classes and dataclasses](01_core/08_classes_and_dataclasses) -
   data models, methods, state, and independent instances.
9. [Exceptions and validation](01_core/09_exceptions_and_validation) -
   parsing, boundary checks, exceptions, and validated dataclasses.
10. [Iterators and generators](01_core/10_iterators_and_generators) -
    one-shot iterables, lazy results, ordering, and immutable updates.
11. [Files and context managers](01_core/11_files_and_context_managers) -
    UTF-8 text I/O, resource management, and deterministic writes.
12. [Modules and standard library](01_core/12_modules_and_standard_library) -
    imports, ISO dates, date arithmetic, and weekdays.
13. [Decorators and closures](01_core/13_decorators_and_closures) -
    wrapped callables, retained state, metadata, and memoization.
14. [Typing and protocols](01_core/14_typing_and_protocols) -
    generics, callables, structural typing, and iterable APIs.
15. [Command-line arguments](01_core/15_command_line_arguments) -
     `argparse` positional and optional parameters with testable `argv`.

## 02 Concurrency and async

1. [Bounded map](02_concurrency_async/01_bounded_map) - thread pools, ordering,
   and exception propagation.
2. [Async pipeline](02_concurrency_async/02_async_pipeline) - queues, workers,
   sentinels, and structured concurrency.

## 03 Software engineering

1. [Configuration](03_software_engineering/01_configuration) - typed
   environment parsing and actionable errors.
2. [Order service](03_software_engineering/02_order_service) - protocols,
   dependency injection, domain rules, and test doubles.
3. [Configuration precedence](03_software_engineering/03_configuration_precedence) -
   defaults, environment variables, explicit overrides, and typed validation.

## 04 Data engineering

1. [Normalize events](04_data_engineering/01_normalize_events) - schema
   normalization, timestamps, deduplication, and data quality.
2. [SQLite warehouse](04_data_engineering/02_sqlite_warehouse) - parameterized
   SQL, idempotent loads, transactions, and aggregation.
3. [Polars lazy aggregations](04_data_engineering/03_polars_lazy_aggregations) -
   typed frames, lazy queries, grouped metrics, and deterministic output.
4. [Parquet projection](04_data_engineering/04_parquet_projection) -
   Arrow schemas, local Parquet I/O, time filters, and column projection.

## 05 AI applications

1. [Vector search](05_ai_applications/01_vector_search) - cosine similarity,
   ranking, and deterministic retrieval.
2. [Retrieval evaluation](05_ai_applications/02_retrieval_evaluation) -
   precision, recall, mean reciprocal rank, and evaluation datasets.
3. [NumPy feature scaling](05_ai_applications/03_numpy_feature_scaling) -
   fitted statistics, immutable parameters, constant columns, and leakage prevention.
4. [PyTorch binary classifier](05_ai_applications/04_pytorch_binary_classifier) -
   tensors, logits, loss functions, gradient descent, and reproducibility.

## Roadmap

Exercises should be added in this order:

| Track | Planned progression |
| --- | --- |
| Core | completed beginner sequence; future additions can cover packaging and network I/O |
| Concurrency | locks and race conditions; process pools; async cancellation; timeouts and retries; rate limiting; producer/consumer backpressure |
| Software engineering | pytest fixtures and parametrization; property testing; CLI design; HTTP APIs; clean architecture; logging and metrics; profiling; security; packaging and releases |
| Data engineering | CSV/JSON/Parquet; pandas and Polars; SQLAlchemy; migrations; incremental ETL; data contracts; partitioning; Kafka; orchestration; distributed processing |
| AI applications | feature engineering; model training; reproducibility; embeddings; chunking; RAG; tool calling; prompt testing; model evaluation; safety; monitoring and serving |

Each addition must follow the contract in [AGENTS.md](../AGENTS.md) and remain
small enough to complete in one focused session.

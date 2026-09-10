# Exercise index

Work through the tracks in order. Within each track, exercise numbers restart
at `01`.

## 01 Core Python

1. [Measurements](track01_core/exercise01_measurements) - dataclasses, parsing, validation,
   comprehensions, and statistics.
2. [Inventory](track01_core/exercise02_inventory) - dictionaries, generators, sorting, and
   immutable result objects.

## 02 Concurrency and async

1. [Bounded map](track02_concurrency_async/exercise01_bounded_map) - thread pools, ordering,
   and exception propagation.
2. [Async pipeline](track02_concurrency_async/exercise02_async_pipeline) - queues, workers,
   sentinels, and structured concurrency.

## 03 Software engineering

1. [Configuration](track03_software_engineering/exercise01_configuration) - typed
   environment parsing and actionable errors.
2. [Order service](track03_software_engineering/exercise02_order_service) - protocols,
   dependency injection, domain rules, and test doubles.

## 04 Data engineering

1. [Normalize events](track04_data_engineering/exercise01_normalize_events) - schema
   normalization, timestamps, deduplication, and data quality.
2. [SQLite warehouse](track04_data_engineering/exercise02_sqlite_warehouse) - parameterized
   SQL, idempotent loads, transactions, and aggregation.

## 05 AI applications

1. [Vector search](track05_ai_applications/exercise01_vector_search) - cosine similarity,
   ranking, and deterministic retrieval.
2. [Retrieval evaluation](track05_ai_applications/exercise02_retrieval_evaluation) -
   precision, recall, mean reciprocal rank, and evaluation datasets.

## Roadmap

Exercises should be added in this order:

| Track | Planned progression |
| --- | --- |
| Core | functions and closures; exceptions; iterators; decorators; context managers; classes and protocols; typing and generics; modules and packaging; file and network I/O |
| Concurrency | locks and race conditions; process pools; async cancellation; timeouts and retries; rate limiting; producer/consumer backpressure |
| Software engineering | pytest fixtures and parametrization; property testing; CLI design; HTTP APIs; clean architecture; logging and metrics; profiling; security; packaging and releases |
| Data engineering | CSV/JSON/Parquet; pandas and Polars; SQLAlchemy; migrations; incremental ETL; data contracts; partitioning; Kafka; orchestration; distributed processing |
| AI applications | feature engineering; model training; reproducibility; embeddings; chunking; RAG; tool calling; prompt testing; model evaluation; safety; monitoring and serving |

Each addition must follow the contract in [AGENTS.md](../AGENTS.md) and remain
small enough to complete in one focused session.

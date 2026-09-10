# Async pipeline

## Theory

An `asyncio.Queue` provides backpressure between producers and consumers.
`TaskGroup` ties worker lifetimes together so failures cancel sibling tasks
instead of leaving background work behind.

## Task

Implement `run_pipeline` with a bounded queue and the requested worker count.
Return results in input order even when processing completes out of order.

## Run

```bash
make exercise EXERCISE=exercises/track02_concurrency_async/exercise02_async_pipeline
```

## Further practice

Add a timeout and expose peak queue depth as a metric.

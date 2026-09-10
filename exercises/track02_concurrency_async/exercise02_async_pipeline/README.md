# Async pipeline

## Theory

An `asyncio.Queue` provides backpressure between producers and consumers.
`TaskGroup` ties worker lifetimes together so failures cancel sibling tasks
instead of leaving background work behind.

## Learn before coding

An `asyncio.Queue(maxsize=2)` provides bounded handoff: `await queue.put(x)`
waits when full, and `item = await queue.get()` receives one value. An async
worker can `result = await transform(item)` and call `queue.task_done()` in a
`finally` block.

- Sketch the pipeline as separate producer, worker, and collector stages.
- Coordinate their lifetimes:
  - Use sentinel values or cancellation to stop workers after production.
  - Use `await queue.join()` to account for every item.
- Preserve input order by tagging values with indexes even when tasks finish
  out of order, and validate positive worker and queue sizes.

## Task

- Implement `run_pipeline` with a bounded queue and the requested worker count.
- Return results in input order even when processing completes out of order.

## Run

```bash
make 02_concurrency_02_async_pipeline
```

## Further practice

Add a timeout and expose peak queue depth as a metric.

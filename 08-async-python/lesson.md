# 08 - Async Python

Async Python is easier to understand once you separate three ideas: concurrency, parallelism, and I/O waiting.

## The mental model

For I/O-heavy work, one thread can keep making progress while another operation is waiting for the network or disk.

```text
Task A ── request ─────────────── response ──┐
                                             │
Task B ── request ── response ──────────────┤──► continue
                                             │
Task C ── request ───────────── response ────┘
```

`async def` creates a coroutine function. `await` gives the event loop a chance to run something else while an awaitable is pending.

## Do not equate async with faster

Async helps when your workload spends meaningful time waiting. It does not make CPU-heavy Python code magically parallel.

## Gathering work

```python
import asyncio


async def fetch_one(client, url):
    ...


async def fetch_all(client, urls):
    return await asyncio.gather(*(fetch_one(client, url) for url in urls))
```

This can turn sequential network calls into concurrent I/O, but you still need limits when calling a real service.

## Practical application: concurrent URL checker

You will build a tool that checks several endpoints and reports their status.

```text
              ┌──► endpoint A ──┐
input URLs ───┼──► endpoint B ──┼──► results
              └──► endpoint C ──┘
                    concurrently
```

The exercise includes an artificial async HTTP function so the tests do not need the public internet.

## Cancellation and limits

Learn to recognize cancellation and bounded concurrency before building a large async service. Starting 10,000 requests at once is usually not a strategy.

## Async in FastAPI

A route can be `async def` when it performs async I/O. If a route calls blocking code, merely adding `async` does not make that blocking code non-blocking.

## Exercise

Implement the starter in `exercises/module08/`.

Requirements:

- check all URLs concurrently
- return results in the same order as the input
- capture timeout/failure as a result rather than aborting the entire batch
- limit concurrency with a semaphore

### Investigation

Look up `asyncio.gather`, `asyncio.Semaphore`, cancellation, and `asyncio.TaskGroup`.

## Documentation

- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [Coroutines and tasks](https://docs.python.org/3/library/asyncio-task.html)
- [Task groups](https://docs.python.org/3/library/asyncio-task.html#task-groups)
- [httpx async support](https://www.python-httpx.org/async/)

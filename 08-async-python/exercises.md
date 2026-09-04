# Exercises - Module 08

## Exercise 1 - Concurrent checks

Implement `check_urls()` so the supplied URLs are checked concurrently.

## Exercise 2 - Preserve order

The checks may complete in any order, but the returned results must match input order.

## Exercise 3 - Bounded concurrency

Use a semaphore to prevent more than `limit` checks from running at once.

## Exercise 4 - Failure isolation

A single timeout or exception should produce a failed result without cancelling unrelated checks.

## Investigation

Compare `asyncio.gather()` and `asyncio.TaskGroup`. Identify one important difference in how failures are handled.

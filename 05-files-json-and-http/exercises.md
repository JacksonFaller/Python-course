# Exercises - Module 05

Use the starter in `exercises/module05/` and the tests in `tests/module05/`.

## Exercise 1 - Fetch JSON

Implement `fetch_json()` with an explicit timeout and correct HTTP error handling.

## Exercise 2 - Save snapshot

Implement `save_json()` so nested output directories are created automatically.

## Exercise 3 - Client design

Implement `ApiSnapshotClient` without putting file-system operations in the HTTP method.

## Investigation

Read the `httpx.Client` documentation and identify one reason a client object can be preferable to repeatedly calling top-level request functions.

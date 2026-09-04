# 04 - Errors, resources, and application structure

The next step is turning small functions into an application you can maintain.

## Exceptions

Python uses exceptions for failures that cannot be handled by the current operation.

```python
class ImportError(Exception):
    pass


def parse_port(value: str) -> int:
    try:
        port = int(value)
    except ValueError as exc:
        raise ImportError(f"Invalid port: {value}") from exc

    if not 1 <= port <= 65535:
        raise ImportError("Port must be between 1 and 65535")
    return port
```

Catch the exception at the boundary where you can actually do something useful with it. Avoid broad `except Exception:` blocks unless you are deliberately building a top-level error boundary.

## Context managers

Resources often need deterministic cleanup. Python's `with` statement is the common pattern:

```python
with open("input.txt", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
```

A context manager can represent much more than a file: locks, database transactions, temporary resources, and library-specific scopes all use the same pattern.

## Logging

For applications, prefer `logging` over scattered `print()` calls.

```python
import logging

logger = logging.getLogger(__name__)
logger.info("Imported %s records", count)
```

Keep configuration near the application boundary. Library code should generally create loggers rather than configure global logging.

## Modules and packages

A useful application should have boundaries based on responsibilities, not on how many functions fit in one file.

```text
app/
├── __main__.py
├── cli.py
├── parser.py
├── processor.py
└── errors.py
```

The `__main__.py` file can make a package runnable with `python -m app`.

## Practical application: report builder

In this module you will build a CLI that reads a CSV file, validates rows, aggregates results, and writes a report.

```text
CSV ──► parse ──► validate ──► aggregate ──► report
          │           │
          └───────────┴── errors are handled at useful boundaries
```

Keep parsing, domain rules, and output separate. Do not make the CLI layer know how aggregation works.

## A C# design instinct to watch

You can absolutely build layers such as CLI → service → repository in Python. The lesson is to choose boundaries because they reduce coupling, not because every application needs a familiar architecture diagram.

## Exercise

Build the starter application in `exercises/module04/`.

Requirements:

- read the supplied CSV file
- reject rows with missing required fields
- normalize emails
- produce a report containing total valid records and records grouped by domain
- use a custom exception for malformed rows
- use `logging` for rejected rows
- keep file handling in a context manager

### Investigation

Look up:

- exception chaining with `raise ... from ...`
- custom context managers
- `logging.Logger.exception()`
- package `__main__.py`

## Documentation

- [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
- [contextlib](https://docs.python.org/3/library/contextlib.html)
- [logging](https://docs.python.org/3/library/logging.html)
- [Modules](https://docs.python.org/3/tutorial/modules.html)

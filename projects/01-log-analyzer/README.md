# Project 01 - Log Analyzer

Your first end-to-end Python project.

Build a CLI that reads web access logs, validates records, aggregates useful metrics, and writes a report.

## What you are practicing

This project combines Modules 01-04:

- dictionaries and collections
- functions and generators
- files and `pathlib`
- exceptions and logging
- modules and packages
- command-line interfaces
- tests

## Input

Use `data/access.log`. The format is intentionally simple:

```text
2026-09-01T10:15:00Z GET /api/orders 200 31
```

Fields are:

```text
timestamp method path status duration_ms
```

## Required output

Your CLI should report:

- total requests
- request count by status class (`2xx`, `4xx`, `5xx`, ...)
- error count by path
- average duration by path
- slowest request

A machine-readable JSON output is recommended.

## Suggested progression

```text
parse one line
    ↓
parse the file
    ↓
validate records
    ↓
calculate metrics
    ↓
format report
    ↓
CLI
    ↓
tests + logging
```

Do not add a database or web framework.

## Starting point

Start with `src/log_analyzer/parser.py` and `src/log_analyzer/report.py`. The tests under `tests/` intentionally leave implementation decisions to you.

The project is considered complete when:

```bash
python -m log_analyzer data/access.log --format json
pytest projects/01-log-analyzer/tests
```

works from the repository root after installing the project.

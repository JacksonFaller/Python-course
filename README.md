# Python for C# Developers

A practical Python course for experienced C# developers.

This course assumes you already know programming, OOP, HTTP, SQL, testing, Git, and general software engineering. It focuses on the parts that are different, idiomatic, or especially useful in Python.

## Goal

By the end, you should be comfortable joining an existing Python backend project, reading unfamiliar Python, building small services and automation tools, working with APIs and databases, writing tests, and packaging an application.

## How to use this repository

Work through the modules in order. Each lesson teaches a small set of concepts. Each exercise is a separate task in `exercises.md` and, when useful, has a runnable starter in `exercises/` plus tests in `tests/`.

A typical exercise loop is:

```text
lesson.md
   ↓
exercises.md
   ↓
open the matching starter in exercises/
   ↓
implement the TODOs
   ↓
pytest tests/...
   ↓
compare with solutions/ only after trying
```

The tests are feedback, not a substitute for reading the task. Some investigation exercises intentionally have no automated answer.

## Course map

| Module | Focus | Main outcome |
| --- | --- | --- |
| 00 | Environment and workflow | Run and structure Python projects |
| 01 | Python mindset | Read and write everyday Python |
| 02 | Functions and data processing | Build small transformation pipelines |
| 03 | Objects and the data model | Model application code idiomatically |
| 04 | Errors, resources, modules | Structure a maintainable CLI app |
| 05 | Files, JSON, HTTP | Build a useful API client |
| 06 | Databases | Work with SQL and SQLAlchemy |
| 07 | FastAPI | Build a production-shaped REST API |
| 08 | Async Python | Understand concurrency in Python |
| 09 | Testing and quality | Test and lint real applications |
| 10 | Typing | Use Python's type system effectively |
| 11 | Packaging and deployment | Ship a Python application |
| 12 | Ecosystem | Know what to learn next |

## Projects

- [Project 01 - Log Analyzer](projects/01-log-analyzer/README.md)
- [Project 02 - Inventory API](projects/02-inventory-api/README.md)
- [Project 03 - Data Integration Service](projects/03-data-integration-service/README.md)

Projects are deliberately less guided than module exercises. Project 01 has a starter and reference implementation; Projects 02 and 03 become progressively more open-ended.

## Setup

Python 3.13+ is recommended.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install the course and development dependencies:

```bash
python -m pip install -e .
python -m pip install --group dev
```

Run all automated checks:

```bash
pytest
ruff check .
mypy exercises/module10
```

## Official documentation

- [Python documentation](https://docs.python.org/3/)
- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Python standard library](https://docs.python.org/3/library/)
- [typing](https://docs.python.org/3/library/typing.html)
- [pytest](https://docs.pytest.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [Ruff](https://docs.astral.sh/ruff/)
- [mypy](https://mypy.readthedocs.io/)
- [Docker Python guide](https://docs.docker.com/language/python/)

## A note for C# developers

You will sometimes see a Python solution that looks less explicit than the equivalent C# code. That does not automatically make it better. The point of the course is to learn when Python's flexibility helps and when explicit structure is worth keeping.

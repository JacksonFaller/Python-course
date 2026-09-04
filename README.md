# Python for C# Developers

A practical Python course for experienced C# developers.

This course assumes you already know programming, OOP, HTTP, SQL, testing, Git, and general software engineering. It focuses on the parts that are different, idiomatic, or especially useful in Python.

## Goal

By the end, you should be comfortable joining an existing Python backend project, reading unfamiliar Python, building small services and automation tools, working with APIs and databases, writing tests, and packaging an application.

## How to use this repository

Work through the modules in order. Do the exercises before opening `solutions/`. When an exercise says to look something up, use the linked official documentation rather than searching for a tutorial immediately.

Each module follows roughly this pattern:

1. Context and the Python/C# difference that matters
2. A small amount of syntax
3. A real application example
4. Exercises
5. A stretch/investigation task
6. Links to documentation

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

### Project 1: Log Analyzer
A CLI application that reads web-server logs, calculates useful metrics, and produces a report.

Skills: collections, functions, files, exceptions, modules, testing, CLI design.

### Project 2: Inventory API
A FastAPI service backed by PostgreSQL/SQLAlchemy.

Skills: HTTP, validation, application structure, persistence, dependency injection, testing, async boundaries.

### Project 3: Data Integration Service
An ingestion pipeline that pulls data from an external API, validates and transforms it, stores it, and exposes selected results through an API.

Skills: integration design, retries, configuration, async I/O, database work, observability, packaging, Docker.

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

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

The course will introduce dependencies as they become useful instead of installing the entire ecosystem on day one.

## Official documentation

- [Python documentation](https://docs.python.org/3/)
- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Python standard library](https://docs.python.org/3/library/)
- [typing](https://docs.python.org/3/library/typing.html)
- [pytest](https://docs.pytest.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [Ruff](https://docs.astral.sh/ruff/)
- [Docker Python guide](https://docs.docker.com/language/python/)

## A note for C# developers

You will sometimes see a Python solution that looks less explicit than the equivalent C# code. That does not automatically make it better. The point of the course is to learn when Python's flexibility helps and when explicit structure is worth keeping.

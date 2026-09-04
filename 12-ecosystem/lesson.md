# 12 - The Python ecosystem

You do not need to memorize the ecosystem. You need a map for finding the right tool.

## Backend

- FastAPI: modern APIs and services
- Django: batteries-included web applications
- Flask: small web applications and lightweight services

## Data

- pandas: tabular analysis and transformation
- NumPy: numerical arrays and scientific computing
- Polars: fast dataframe workflows

## Automation and systems

- pathlib: filesystem work
- subprocess: external processes
- argparse / Typer: CLI applications
- httpx: HTTP clients

## Infrastructure and reliability

- SQLAlchemy: database access
- Pydantic: parsing and validation
- structlog/logging: application logs
- OpenTelemetry: distributed tracing and metrics concepts

The important skill is reading the official documentation, checking maintenance/activity, and understanding the abstraction before adding a dependency.

## Choosing a library

Use this sequence:

```text
standard library enough?
       │
      yes ──► use it
       │
       no
       ▼
well-supported library?
       │
       ▼
check API + maintenance + license + fit
       │
       ▼
add the smallest useful dependency
```

## Final exercise

Pick one problem from your own work that could benefit from Python. Do not write code immediately. Produce a one-page design containing:

- input/output boundaries
- libraries you would use
- what should remain standard library code
- where failures are handled
- what you would test
- one thing you intentionally would *not* abstract yet

Then implement a small vertical slice.

### Investigation

Choose one library you have never used. Read its official quickstart and API reference. Find one design choice you would question in a production review.

## Documentation

- [Python Packaging User Guide](https://packaging.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Django](https://docs.djangoproject.com/)
- [Flask](https://flask.palletsprojects.com/)
- [pandas](https://pandas.pydata.org/docs/)
- [Polars](https://docs.pola.rs/)
- [Typer](https://typer.tiangolo.com/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)

# 06 - Databases: SQL first, ORM second

As a C# developer, you probably know the shape of ORM code already. This module focuses on how database access feels in Python and why SQLAlchemy is structured the way it is.

## Start with SQL

Python's `sqlite3` module is enough to expose the basic mechanics:

```python
import sqlite3

with sqlite3.connect("app.db") as connection:
    connection.execute(
        "insert into users (name) values (?)",
        ("Ada",),
    )
```

Parameters are values, not string concatenation.

## Transactions

A transaction is still a database concept, not a Python concept. Learn what your connection/context manager is doing rather than assuming `with` always means "commit everything" in every library.

## SQLAlchemy

SQLAlchemy has multiple layers. You can work with SQL expressions and with the ORM.

```python
from sqlalchemy import select

statement = select(User).where(User.email == email)
```

You do not need to memorize the entire API. Learn the session/unit-of-work model and how SQL is ultimately produced.

## Practical application: inventory repository

We will turn the Module 03 inventory domain into persistent storage.

```text
Warehouse domain
      │
      ▼
 Repository
      │
      ▼
 SQLAlchemy
      │
      ▼
 PostgreSQL / SQLite for local tests
```

The repository should hide persistence details from the domain logic, while avoiding a giant abstraction that merely repeats every ORM method.

## Exercise

Implement the starter in `exercises/module06/`.

Requirements:

- define a SQLAlchemy model for products
- create a database/session factory
- implement repository methods to add, fetch, and update stock
- persist transactions correctly
- write tests against SQLite

The starter deliberately uses a synchronous session. Async database access comes later.

### Investigation

Read about SQLAlchemy's `Session`, `select()`, `session.scalars()`, and transaction behavior.

## Documentation

- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/20/orm/)
- [SQLAlchemy session basics](https://docs.sqlalchemy.org/en/20/orm/session_basics.html)
- [SQLAlchemy select](https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html)

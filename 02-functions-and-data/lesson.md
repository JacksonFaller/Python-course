# 02 - Functions and data processing

Python becomes especially productive when functions, iterables, and generators are combined into small data-processing steps.

## 1. Keyword arguments

Python functions can be called by parameter name:

```python
def create_user(name: str, active: bool = True) -> dict:
    return {"name": name, "active": active}

create_user("Ada", active=False)
```

This can make call sites self-documenting. You will also encounter positional-only and keyword-only parameters in mature libraries; look them up when you encounter the syntax.

## 2. Functions should express an operation

Consider a batch-processing job:

```python
def calculate_total(order):
    return sum(item["price"] * item["quantity"] for item in order["items"])
```

The generator expression inside `sum()` avoids constructing an intermediate list.

## 3. Iterables and generators

A list contains values now. A generator describes how to produce values as they are consumed.

```python
def successful_ids(requests):
    for request in requests:
        if request["status"] == "success":
            yield request["id"]
```

This distinction matters when processing large files or streams.

```text
file
 │
 ▼
iterator ──► transform ──► filter ──► output
                 │
                 └── values are processed as needed
```

Don't reach for generators just because they exist. Use them when deferred processing or streaming is useful.

## 4. `enumerate` and `zip`

Avoid manually maintaining indexes:

```python
for index, line in enumerate(lines, start=1):
    print(index, line)
```

Pair related iterables with `zip`:

```python
for user, role in zip(users, roles):
    assign_role(user, role)
```

## 5. A real application: import pipeline

Suppose a service imports records from a CSV export. The application needs to parse records, reject malformed records, normalize values, calculate derived fields, and produce records ready for persistence.

Keep each step small:

```python
def normalize_email(value: str) -> str:
    return value.strip().lower()


def is_valid(record: dict) -> bool:
    return bool(record.get("email")) and bool(record.get("name"))


def prepare(record: dict) -> dict:
    return {
        "name": record["name"].strip(),
        "email": normalize_email(record["email"]),
    }


def prepare_records(records):
    return [prepare(record) for record in records if is_valid(record)]
```

This is a small pipeline, but the same shape appears in ETL jobs, API integrations, background workers, and command-line utilities.

## 6. Don't overuse `map` and `filter`

Python has `map()` and `filter()`, but comprehensions are often easier to read for straightforward transformations. Learn both because you will encounter them in existing code.

## 7. `*args` and `**kwargs`

You will see these in framework and library APIs.

```python
def log_event(message: str, *tags: str, **metadata: str) -> None:
    ...
```

Do not use them merely to make an API flexible. Explicit parameters are usually easier to understand.

## What's next

Open [`exercises.md`](exercises.md). The log-processing task has a ready-to-run starter and tests; some of the investigation tasks are intentionally open-ended.

## Documentation

- [Functional programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Built-in functions](https://docs.python.org/3/library/functions.html)
- [itertools](https://docs.python.org/3/library/itertools.html)
- [collections](https://docs.python.org/3/library/collections.html)
- [statistics](https://docs.python.org/3/library/statistics.html)

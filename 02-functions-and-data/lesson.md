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

Suppose a service imports records from a CSV export. The application needs to:

1. parse records
2. reject malformed records
3. normalize values
4. calculate derived fields
5. produce records ready for persistence

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

Python has `map()` and `filter()`, but comprehensions are often easier to read for straightforward transformations.

Prefer:

```python
active = [user for user in users if user["active"]]
```

over an unnecessarily indirect expression. Learn both because you will encounter them in existing code.

## 7. `*args` and `**kwargs`

You will see these in framework and library APIs.

```python
def log_event(message: str, *tags: str, **metadata: str) -> None:
    ...
```

Do not use them merely to make an API flexible. Explicit parameters are usually easier to understand.

## Exercise - log processing pipeline

You are given web access logs represented as dictionaries:

```python
logs = [
    {"path": "/api/orders", "status": 200, "duration_ms": 31},
    {"path": "/api/orders", "status": 500, "duration_ms": 91},
    {"path": "/api/users", "status": 200, "duration_ms": 18},
    {"path": "/api/orders", "status": 200, "duration_ms": 42},
]
```

Build functions that:

1. return only failed requests (`status >= 500`)
2. return the slowest request
3. calculate average duration by path
4. calculate an error count by path

Keep each operation separate. Then write a function that produces one report from the four operations.

### Stretch

Change the implementation so the input can be an iterator rather than a list. Think about which operations require more than one pass over the data.

### Investigation

Look up:

- `collections.Counter`
- `collections.defaultdict`
- `statistics.fmean`
- generator expressions
- `itertools.groupby`

Decide which are useful for this problem and why.

## Documentation

- [Functional programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Built-in functions](https://docs.python.org/3/library/functions.html)
- [itertools](https://docs.python.org/3/library/itertools.html)
- [collections](https://docs.python.org/3/library/collections.html)
- [statistics](https://docs.python.org/3/library/statistics.html)

# 05 - Files, JSON, and HTTP

Backend work is often about moving data between systems. Python's standard library handles a surprising amount of this directly.

## `pathlib`

Prefer `Path` for filesystem work:

```python
from pathlib import Path

root = Path("data")
for file in root.glob("*.json"):
    print(file)
```

Learn the object rather than memorizing path-string manipulation.

## JSON

```python
import json

payload = json.loads('{"name": "Ada"}')
text = json.dumps(payload, indent=2)
```

Serialization is a boundary. Validate and normalize data there instead of letting arbitrary dictionaries leak through the whole application.

## HTTP

For exercises we will use `httpx`, because it gives a clean synchronous and asynchronous API and will reappear in the FastAPI/async modules.

```python
import httpx

response = httpx.get("https://example.com", timeout=10)
response.raise_for_status()
data = response.json()
```

A real API client should make timeouts explicit and treat non-success responses deliberately.

## Practical application: API snapshot tool

You will build a small CLI that fetches JSON from an HTTP endpoint and saves a timestamped snapshot.

```text
HTTP API
   │
   ▼
client ──► validate/normalize ──► JSON file
   │
   └──────── errors/timeouts
```

The interesting part is not making one HTTP request. It is deciding where networking, serialization, and file-system concerns belong.

## Exercise

Implement the starter in `exercises/module05/`.

Requirements:

- request JSON from a supplied URL
- use a timeout
- treat non-2xx responses as failures
- write pretty-printed JSON to the supplied output path
- create the output directory if necessary
- keep HTTP code separate from file-writing code

### Investigation

Look up `httpx.Client`, `response.raise_for_status()`, `pathlib.Path.mkdir()`, and JSON serialization options.

## Documentation

- [pathlib](https://docs.python.org/3/library/pathlib.html)
- [json](https://docs.python.org/3/library/json.html)
- [httpx](https://www.python-httpx.org/)

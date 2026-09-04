# 07 - FastAPI: build a real REST API

Now the previous pieces become a service.

## Path operations

A FastAPI route can be as small as:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
```

The framework turns the function signature and decorators into an HTTP interface and OpenAPI schema.

## Request models

Use Pydantic models at the HTTP boundary:

```python
from pydantic import BaseModel


class ProductCreate(BaseModel):
    sku: str
    name: str
    quantity: int = 0
```

Validation belongs at boundaries. Domain rules still belong in domain/application code.

## Dependency injection

FastAPI dependencies are a mechanism for supplying request-scoped or application-scoped things such as database sessions.

Do not confuse framework dependency injection with a mandate to build an elaborate service-container architecture.

## Application structure

```text
app/
├── main.py
├── api.py
├── models.py
├── repository.py
└── schemas.py
```

For a larger service, split by feature rather than endlessly multiplying generic `services/` and `repositories/` folders.

## Practical project: Inventory API

You will convert the inventory repository into a REST service.

```text
HTTP
 ↓
FastAPI route
 ↓
Pydantic schema
 ↓
application logic
 ↓
repository
 ↓
database
```

## Exercise

Implement the starter in `exercises/module07/`.

Endpoints:

- `GET /products/{sku}`
- `POST /products`
- `PATCH /products/{sku}/quantity`
- `GET /health`

Return sensible HTTP status codes. The tests use FastAPI's test client.

### Investigation

Look up FastAPI's `Depends`, response models, HTTP exception handling, and testing documentation.

## Documentation

- [FastAPI](https://fastapi.tiangolo.com/)
- [Request body](https://fastapi.tiangolo.com/tutorial/body/)
- [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [Pydantic](https://docs.pydantic.dev/)

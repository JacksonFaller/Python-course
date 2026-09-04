# 09 - Testing and code quality

Testing is not a Python-specific skill. The useful differences are the tools and the style.

## pytest

A test can be just a function with an assertion:

```python
def test_total():
    assert calculate_total([2, 3]) == 6
```

There is no required test-class ceremony. Fixtures provide reusable setup.

```python
import pytest


@pytest.fixture
def product():
    return {"sku": "A-1", "quantity": 5}
```

Use fixtures for meaningful shared setup, not every value that could be created locally.

## Parameterized tests

When the same rule has multiple examples, parameterization makes the cases visible without copy/paste.

## Mocking

Mock at the boundary you own. If a function calls an HTTP client, test the function's behavior without requiring the public internet.

Do not mock every internal function simply because it is possible.

## Integration tests

Unit tests answer focused questions. Integration tests answer whether your components work together. The course projects will use both.

```text
unit tests             integration tests
    │                         │
    ▼                         ▼
small rules          API + DB + dependencies
```

## Static quality tools

Ruff handles formatting/linting and can catch many mistakes early. Type checkers such as Pyright or mypy add another layer later in the course.

These tools are part of the development loop, not a substitute for understanding the code.

## Exercise

Use the existing Module 07 API and improve its test suite.

Requirements:

- add parameterized validation tests
- test duplicate creation
- test update behavior
- add one integration-style test that exercises multiple endpoints in sequence
- run pytest and Ruff locally

### Investigation

Look up pytest fixtures, `pytest.mark.parametrize`, monkeypatching, and `pytest.raises`.

## Documentation

- [pytest](https://docs.pytest.org/)
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [pytest parametrization](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [Ruff](https://docs.astral.sh/ruff/)

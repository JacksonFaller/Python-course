# 10 - Type hints without turning Python into C#

Python type annotations are primarily information for tools and readers. They are not a general runtime enforcement mechanism.

## Basic annotations

```python
def get_name(user: dict[str, str]) -> str:
    return user["name"]
```

Modern Python supports expressive built-in generic syntax such as `list[str]` and union syntax such as `str | None`.

## Type aliases and structured data

A `TypedDict` is useful when dictionaries are part of a boundary but you still want static checking of their keys.

```python
from typing import TypedDict


class UserPayload(TypedDict):
    name: str
    email: str
```

For domain data, a dataclass or Pydantic model may be more appropriate. These are different tools for different boundaries.

## Protocols

Protocols describe behavior:

```python
from typing import Protocol


class Clock(Protocol):
    def now(self) -> float: ...
```

Any object with a compatible `now()` method can satisfy the protocol for static typing purposes.

## Generics

You will encounter generic classes and functions in libraries. Learn enough to read them before attempting sophisticated type-level designs.

## The important trade-off

Typing should improve the API you have, not make a small Python function resemble a C# interface hierarchy.

```text
untyped Python ──► useful annotations ──► static checking
       │                    │                    │
       └──── runtime behavior remains Python ──┘
```

## Exercise

Use `exercises/module10/` to type a small repository boundary.

Requirements:

- define a `User` model
- define a repository `Protocol`
- type a function that accepts any repository implementing the protocol
- run a static type checker locally

### Investigation

Compare `TypedDict`, dataclasses, Pydantic models, and protocols. Note what is checked statically and what is enforced at runtime.

## Documentation

- [typing](https://docs.python.org/3/library/typing.html)
- [Type hints](https://docs.python.org/3/library/typing.html)
- [TypedDict](https://docs.python.org/3/library/typing.html#typing.TypedDict)
- [Protocols](https://docs.python.org/3/library/typing.html#typing.Protocol)
- [Pyright](https://microsoft.github.io/pyright/)
- [mypy](https://mypy.readthedocs.io/)

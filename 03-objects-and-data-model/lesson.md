# 03 - Objects and Python's data model

Python supports classes and inheritance, but idiomatic Python often uses simpler data structures, composition, and protocols instead of deep class hierarchies.

## 1. A class

```python
class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def display_name(self) -> str:
        return self.name.title()
```

There is no `private` keyword equivalent to C#'s access modifiers. Naming conventions communicate intent, and Python's object model is more dynamic.

## 2. Dataclasses

For data-oriented objects, `dataclass` removes a lot of boilerplate:

```python
from dataclasses import dataclass


@dataclass
class Product:
    sku: str
    name: str
    price: float
```

This is worth learning early. You will encounter it frequently.

## 3. Properties

Python properties let an attribute-looking API execute logic:

```python
class Account:
    def __init__(self, balance: float) -> None:
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance
```

Setters exist, but don't automatically create a property for every field as you might in a typical C# DTO/entity.

## 4. Composition before inheritance

Imagine an order-processing service:

```text
OrderService
 ├── PricingPolicy
 ├── TaxCalculator
 └── OrderRepository
```

Each dependency can expose the behavior `OrderService` needs. Python's structural typing makes this especially useful.

## 5. Protocols

A protocol describes an interface by behavior rather than requiring explicit inheritance.

```python
from typing import Protocol


class OrderRepository(Protocol):
    def save(self, order: "Order") -> None:
        ...
```

A class can satisfy this protocol without inheriting from it. Static type checkers can use that information even though Python itself does not enforce it at runtime.

We will revisit this in the typing module.

## 6. Dunder methods

Python objects participate in language operations through special methods:

```python
class Money:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def __add__(self, other: "Money") -> "Money":
        return Money(self.amount + other.amount)
```

You do not need to memorize these methods. Learn to recognize them and look up the relevant data-model documentation when needed.

## 7. A practical domain model

Build a small inventory domain:

```python
from dataclasses import dataclass


@dataclass
class Product:
    sku: str
    name: str
    quantity: int

    def reserve(self, amount: int) -> None:
        if amount > self.quantity:
            raise ValueError("Not enough stock")
        self.quantity -= amount
```

The object contains data and the operation that protects its invariant. This is useful when the behavior genuinely belongs to the object.

Don't create a class just to wrap a dictionary because the language lets you.

## What's next

Open [`exercises.md`](exercises.md). The inventory exercise has a starter domain model and tests for the expected behavior.

## Documentation

- [Classes](https://docs.python.org/3/tutorial/classes.html)
- [dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [abc](https://docs.python.org/3/library/abc.html)
- [typing.Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)
- [Data model](https://docs.python.org/3/reference/datamodel.html)

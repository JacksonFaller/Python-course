# 01 - The Python mindset

This is the module where Python starts to feel different from C#.

The objective is not to memorize syntax. It is to become comfortable reading ordinary Python and to understand a few language behaviors that strongly affect how you write code.

## 1. Names point at objects

In C#, a variable declaration communicates a static type:

```csharp
Customer customer = service.GetCustomer();
```

Python assignment binds a name to an object:

```python
customer = service.get_customer()
```

The distinction matters because Python names can be rebound and several names can refer to the same mutable object.

```python
items = []
other = items
other.append("order-123")

assert items == ["order-123"]
```

Don't turn this into a philosophical discussion yet. Just recognize aliasing when you see it.

## 2. The core collections

You will use these constantly:

```python
names = ["Ada", "Grace"]              # list
coordinates = (40.7, -74.0)            # tuple
tags = {"python", "backend"}          # set
user = {"id": 42, "name": "Ada"}      # dict
```

A dictionary is a general-purpose workhorse. A list is an ordered collection. A tuple is useful for a fixed grouping of values. A set is useful when membership and uniqueness matter.

Don't assume Python's collection choices map one-to-one to C# collection types. Learn their behavior instead.

## 3. `None` and truthiness

`None` represents the absence of a value.

Python also has truthiness. Empty collections, `0`, `False`, and `None` are falsey.

```python
if not orders:
    print("No orders")
```

This is convenient, but don't use it when the distinction between "empty" and "missing" matters.

For example:

```python
if value is None:
    ...
```

Use `is` for identity checks such as `None`; use `==` for value equality.

## 4. Comprehensions

A common Python pattern is to construct a collection directly from an iterable.

```python
active_emails = [
    user["email"]
    for user in users
    if user["active"]
]
```

This is roughly comparable to a small LINQ pipeline, but it is a native Python idiom.

Don't force everything into a comprehension. If the expression becomes difficult to read, use a normal loop or a named function.

## 5. Unpacking

Python makes it easy to split a sequence into names:

```python
first, second = ["Ada", "Grace"]
```

and to collect the remainder:

```python
first, *middle, last = values
```

You will see this frequently in real code.

## 6. Functions are values

Functions can be passed around like other objects.

```python
def normalize_email(value: str) -> str:
    return value.strip().lower()

normalizer = normalize_email
```

This is one of the foundations for decorators, callbacks, dependency injection patterns, and functional-style utilities later in the course.

## 7. A real example: request filtering

Imagine an API endpoint receiving a batch of requests for processing:

```python
requests = [
    {"id": 1, "status": "ready", "owner": "alice"},
    {"id": 2, "status": "failed", "owner": "bob"},
    {"id": 3, "status": "ready", "owner": "alice"},
]

ready_ids = [request["id"] for request in requests if request["status"] == "ready"]
```

Now turn that into a function:

```python
def ready_request_ids(requests: list[dict]) -> list[int]:
    return [request["id"] for request in requests if request["status"] == "ready"]
```

This is deliberately simple. Later, typing and data models will let us make this safer without losing Python's concise style.

## Exercise mindset

For the exercises, first write the straightforward solution. Then ask whether Python has a standard construct that makes the intent clearer.

Do not optimize for the fewest lines.

## C# developer traps

Keep an eye out for:

- `is` versus `==`
- mutable objects and aliases
- truthiness
- mutable default arguments
- modifying a list while iterating over it
- accidentally creating a tuple with a trailing comma
- assuming a type annotation enforces a runtime type

You will encounter these naturally as the course progresses.

## Exercise

Build a small **order summary** function.

Input:

```python
orders = [
    {"id": 101, "customer": "alice", "total": 120.50, "status": "paid"},
    {"id": 102, "customer": "bob", "total": 80.00, "status": "pending"},
    {"id": 103, "customer": "alice", "total": 45.25, "status": "paid"},
    {"id": 104, "customer": "bob", "total": 30.00, "status": "cancelled"},
]
```

Implement:

```python
def summarize_paid_orders(orders):
    ...
```

It should return the total amount and number of paid orders for each customer.

For the data above, the result should communicate that Alice has two paid orders totaling `165.75` and Bob has no paid orders.

Do not worry about perfect typing yet.

### Stretch

Return the paid orders grouped by customer rather than just the totals.

### Investigation

Look up `dict.get()` and `collections.defaultdict`. Reimplement the grouping without using `if customer not in result`.

## Documentation

- [Built-in types](https://docs.python.org/3/library/stdtypes.html)
- [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [collections](https://docs.python.org/3/library/collections.html)

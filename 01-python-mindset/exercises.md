# Exercises - Module 01

## Exercise 1 - Customer lookup

Given:

```python
customers = [
    {"id": 1, "name": "Alice", "active": True},
    {"id": 2, "name": "Bob", "active": False},
    {"id": 3, "name": "Carol", "active": True},
]
```

Implement functions that:

1. Return all active customer names.
2. Find a customer by ID.
3. Return a dictionary mapping IDs to names.

Use ordinary loops first, then rewrite the parts where a comprehension makes the intent clearer.

## Exercise 2 - Normalize configuration

Given a dictionary containing optional configuration values, write a function that returns normalized values:

- missing `host` -> `localhost`
- missing `port` -> `8080`
- missing `debug` -> `False`

Research `dict.get()` before writing nested conditionals.

## Exercise 3 - Aliasing investigation

Run this code and explain why the output changes:

```python
original = [1, 2, 3]
copy = original
copy.append(4)
print(original)
```

Then research at least two ways to create an independent copy and identify when a shallow copy is insufficient.

## Exercise 4 - Paid order summary

Complete the exercise from the lesson. Add tests yourself using plain `assert` statements for at least three cases:

- normal input
- no paid orders
- empty input

# Exercises - Module 10

## Exercise 1 - Typed repository

Implement the missing annotations in `exercises/module10/repository.py`.

## Exercise 2 - Protocol

Make `InMemoryUserRepository` satisfy `UserRepository` without explicitly inheriting from it.

## Exercise 3 - Check it

Run mypy against the exercise directory. Introduce one deliberate type error, observe it, then fix it.

```bash
mypy exercises/module10
```

## Investigation

Find one example where `TypedDict` is preferable to a dataclass and one where a dataclass is preferable to `TypedDict`.

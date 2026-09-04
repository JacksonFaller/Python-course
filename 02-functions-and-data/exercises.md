# Exercises - Module 02

## Exercise 1 - Order totals

Implement:

```python
def calculate_total(order):
    ...
```

Use a generator expression inside `sum()`.

## Exercise 2 - Log report

Complete the log-processing exercise from the lesson. Add at least five records of your own, including a path that has no errors.

## Exercise 3 - Streaming input

Create a generator that reads a text file one line at a time and yields only lines containing `ERROR`.

Do not call `.read()` or `.readlines()`.

## Exercise 4 - Refactor

Start with a loop-based implementation of one of your earlier exercises. Refactor it only where a comprehension or generator makes the intent clearer. Keep the loop if the transformation becomes harder to read.

## Investigation

Find out what happens when `zip()` receives iterables of different lengths. Decide whether that behavior is appropriate for a data-import pipeline and find a standard-library alternative if you need stricter handling.

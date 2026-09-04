# Exercises - Module 02

These exercises use runnable templates and tests. Start in `../exercises/module02/`.

## Exercise 1 - Order totals

Complete `order_totals.py`. Use a generator expression inside `sum()`.

## Exercise 2 - Log report

Complete `log_report.py`: failed requests, slowest request, average duration by path, error count by path, and a combined report. The tests define the expected report shape.

### Stretch

Make the public functions work with iterators rather than requiring a list. Think about which calculations need more than one pass.

## Exercise 3 - Streaming input

Complete `error_lines.py`. Read a text file one line at a time and yield only lines containing `ERROR`. Do not use `.read()` or `.readlines()`.

## Exercise 4 - Refactor

`refactor.py` contains an intentionally loop-heavy implementation. Refactor only where a comprehension or generator makes the intent clearer.

## Investigation

Look up what happens when `zip()` receives iterables of different lengths. Decide whether that behavior is suitable for a data-import pipeline and find a standard-library alternative if stricter handling is required.

## Documentation

- [Functional programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Built-in functions](https://docs.python.org/3/library/functions.html)
- [itertools](https://docs.python.org/3/library/itertools.html)
- [collections](https://docs.python.org/3/library/collections.html)
- [statistics](https://docs.python.org/3/library/statistics.html)

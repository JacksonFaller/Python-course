# Exercises - Module 01

The lesson is separate from the hands-on work. Start with the templates under `../exercises/module01/` and run `python -m pytest` as you work.

## Exercise 1 - Customer lookup

Complete `customer_lookup.py`: return active customer names, find a customer by ID (or `None`), and build an ID-to-name dictionary.

## Exercise 2 - Normalize configuration

Complete `config.py`. Missing values should default to `host=localhost`, `port=8080`, and `debug=False`. Look up `dict.get()` before writing nested conditionals.

## Exercise 3 - Aliasing investigation

Complete `aliasing.py` by adding shallow and deep copy helpers. Research when a shallow copy is insufficient. This exercise is intentionally not test-driven.

## Exercise 4 - Paid order summary

Complete `order_summary.py`. Return `{customer: {"count": int, "total": float}}` for customers with paid orders. Tests cover normal input, empty input, and customers with no paid orders.

### Stretch

Implement the same grouping with `collections.defaultdict`.

### Investigation

Compare `dict.get()` and `collections.defaultdict` and decide where each is clearer.

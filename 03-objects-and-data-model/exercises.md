# Exercises - Module 03

Start with `../exercises/module03/inventory.py` and run the tests in `../tests/module03/`.

## Exercise 1 - Inventory

Implement a `Warehouse` that supports adding products, lookup by SKU, receiving stock, and reserving stock. Handle duplicate SKUs, non-positive quantities, unknown SKUs, and over-reservation deliberately. Use `InsufficientStockError` for stock violations.

## Exercise 2 - Repository protocol

Add an in-memory repository with `save(product)` and `get(sku)` and define a `Protocol` for it. The implementation should satisfy the protocol without inheriting from it.

## Exercise 3 - Class or dictionary?

Take customer/order code from Module 01 and model the domain with a dataclass. Compare it with the dictionary-based version and note what became clearer or more cumbersome.

## Documentation

- [Classes](https://docs.python.org/3/tutorial/classes.html)
- [dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [typing.Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

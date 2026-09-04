# Exercises - Module 03

## Exercise 1 - Inventory

Implement the warehouse scenario from the lesson.

Requirements:

- adding a duplicate SKU should be handled deliberately
- receiving a non-positive quantity should fail
- reserving more than available should fail
- unknown SKUs should produce a useful error

Do not worry about creating a full exception hierarchy.

## Exercise 2 - Repository protocol

Create an in-memory repository with:

```python
save(product)
get(sku)
```

Define a protocol describing those operations. Confirm that your repository does not need to inherit from the protocol.

## Exercise 3 - Decide whether a class is warranted

Take one earlier exercise that uses dictionaries. Rewrite it using a dataclass, then compare the two versions. Decide which one communicates the domain better and why.

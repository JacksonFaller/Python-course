# Project 02 - Inventory API

Build a REST API for warehouse inventory.

This project is intentionally less guided than Project 01. Use Modules 03, 06, 07, 09, and 10 as references, but make the architecture decisions yourself.

## Scenario

A warehouse needs an API to manage products and stock reservations.

## Required endpoints

Implement at least:

```text
GET    /products
GET    /products/{sku}
POST   /products
POST   /products/{sku}/receive
POST   /products/{sku}/reserve
DELETE /products/{sku}
```

## Requirements

Products have at least:

- SKU
- name
- quantity
- price

The API should validate input and return appropriate HTTP status codes. Persist data in a relational database using SQLAlchemy.

Add tests for normal behavior and failure cases.

## Suggested milestones

1. In-memory API
2. request/response models
3. database persistence
4. error handling
5. tests
6. configuration
7. Docker
8. optional async database/API work

## Design constraints

Keep the first version small. You do not need CQRS, a generic repository base class, or a large dependency-injection framework.

A reasonable shape is:

```text
HTTP
 ↓
API layer
 ↓
domain/service logic
 ↓
SQLAlchemy persistence
 ↓
PostgreSQL
```

You can change this when you have a reason.

## Definition of done

A new developer should be able to clone the repository, start the API, initialize the database, run the tests, and understand the API through its generated OpenAPI documentation.

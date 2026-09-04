# Exercises - Module 07

## Exercise 1 - Health endpoint

Run the starter and make the health endpoint return the expected payload.

## Exercise 2 - Create product

Implement validation and persistence for `POST /products`.

## Exercise 3 - Read and update

Implement lookup and quantity updates, including a 404 for unknown SKUs.

## Exercise 4 - Boundary design

Find one business rule that should not live in the FastAPI route. Move it into application/domain code and add a focused unit test.

## Investigation

Read the FastAPI documentation for `Depends` and explain to yourself what object lifetime you want for a database session during one request.

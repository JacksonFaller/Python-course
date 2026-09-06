# Exercises - Module 11

## Exercise 1 - Package metadata

Read the existing `pyproject.toml` and identify where runtime and development dependencies are represented.

## Exercise 2 - Docker

Complete `exercises/module11/Dockerfile` for the FastAPI application.

## Exercise 3 - CI

Complete `11-packaging-and-deployment/ci-example.yml` as a GitHub Actions workflow example. It should upgrade pip as needed, install the project with its `dev` dependency group, run pytest, and run Ruff.

In a real repository, where would this file need to live for GitHub Actions to run it automatically?

## Investigation

Find out why an editable install is useful during local development and what changes in a production container.

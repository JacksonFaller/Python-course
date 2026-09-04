# Exercises - Module 04

The runnable starter is in `exercises/module04/`.

## Exercise 1 - CSV importer

Implement the functions marked `TODO` in `importer.py`.

The tests in `tests/module04/` describe the expected behavior.

## Exercise 2 - Error boundary

Add a CLI entry point that returns a non-zero exit code for invalid input while keeping the validation exception out of the command-line parsing code.

## Exercise 3 - Logging

Add useful warning messages for rejected rows. Do not log the user's full record; include enough context to diagnose the problem.

## Investigation

Find out how `logging` propagates through the logger hierarchy and how `propagate` affects it.

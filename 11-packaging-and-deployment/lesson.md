# 11 - Packaging and deployment

You have enough Python knowledge to write applications. Now make them easy to install and run.

## `pyproject.toml`

Use it as the project metadata and tool configuration boundary. Dependencies belong to the project rather than being documented only in a README.

The repository root already contains a minimal `pyproject.toml`.

## Packages and entry points

A package can expose a command-line entry point instead of requiring users to know the Python file layout. Learn this when you turn the Log Analyzer into a distributable tool.

## Docker

A Python container should have a predictable interpreter, installed dependencies, and one clear application command.

```text
Docker image
├── Python runtime
├── application package
├── installed dependencies
└── entrypoint
```

## Configuration

Use environment variables or an application settings mechanism for deployment-specific values. Do not hard-code secrets in source control.

## CI

A useful minimal pipeline runs:

```text
install → test → lint → build
```

Later you can add integration tests and container builds.

## Exercise

Create a Dockerfile for the Module 07 API and add a GitHub Actions workflow that runs pytest and Ruff.

Requirements:

- install the project from `pyproject.toml`
- run tests in CI
- run Ruff in CI
- expose the API port in the container
- use an explicit application command

### Investigation

Look up editable installs, package discovery, Docker multi-stage builds, and GitHub Actions Python setup.

## Documentation

- [Python packaging user guide](https://packaging.python.org/)
- [pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [Docker Python guide](https://docs.docker.com/language/python/)
- [GitHub Actions: Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)

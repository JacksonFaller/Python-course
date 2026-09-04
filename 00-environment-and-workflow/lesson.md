# 00 - Environment and workflow

## Objective

Get a Python project running and understand the basic workflow. This module is intentionally short.

## 1. Python is an executable, not a project template

A `.py` file can be run directly:

```bash
python hello.py
```

A directory can also be treated as a package/module and run with `-m`:

```bash
python -m myapp
```

That distinction becomes useful once the course starts using packages.

## 2. Virtual environments

A virtual environment keeps project dependencies isolated.

```bash
python -m venv .venv
```

Activate it, then install packages into that environment. You generally do not want project dependencies installed globally.

Check which interpreter is active:

```bash
python --version
python -c "import sys; print(sys.executable)"
```

### C# comparison

Think of a virtual environment as part of the project's dependency boundary, but don't map it directly onto a `.csproj`. Python dependency management has its own conventions.

## 3. `pyproject.toml`

Modern Python projects commonly keep project metadata and tool configuration in `pyproject.toml`. We will use it more seriously later.

For now, recognize it as the central configuration file rather than trying to memorize its schema.

## 4. Your first tiny application

Create a directory containing:

```text
hello-python/
├── .venv/
└── hello.py
```

`hello.py`:

```python
from datetime import datetime


def main() -> None:
    print(f"Python is running: {datetime.now():%Y-%m-%d %H:%M:%S}")


if __name__ == "__main__":
    main()
```

Don't worry about every detail yet. You will meet functions, imports, annotations, and the `__name__` convention properly in later modules.

Run it. Then deliberately break the import and observe the error. Python's traceback is part of your development workflow; get used to reading it from the bottom upward.

## What to practice

Use `00-environment-and-workflow/exercises.md` for hands-on work. There is intentionally little starter code here because several exercises are about observing your local interpreter and module behavior.

## Documentation

- [venv](https://docs.python.org/3/library/venv.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [pathlib](https://docs.python.org/3/library/pathlib.html)
- [Python command-line interface](https://docs.python.org/3/using/cmdline.html)

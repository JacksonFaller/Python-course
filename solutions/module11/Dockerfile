FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml .
COPY exercises ./exercises

RUN pip install --no-cache-dir fastapi uvicorn pydantic

CMD ["uvicorn", "exercises.module07.app:app", "--host", "0.0.0.0", "--port", "8000"]

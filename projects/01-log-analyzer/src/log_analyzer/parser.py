from datetime import datetime

from .models import LogEntry


class InvalidLogEntry(ValueError):
    pass


def parse_line(line: str) -> LogEntry:
    parts = line.strip().split()
    if len(parts) != 5:
        raise InvalidLogEntry(f"Expected 5 fields, got {len(parts)}")

    timestamp, method, path, status_text, duration_text = parts
    try:
        status = int(status_text)
        duration_ms = int(duration_text)
        parsed_timestamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError as exc:
        raise InvalidLogEntry(f"Invalid log entry: {line.strip()}") from exc

    if not method or not path or duration_ms < 0 or not 100 <= status <= 599:
        raise InvalidLogEntry(f"Invalid log entry: {line.strip()}")

    return LogEntry(parsed_timestamp, method, path, status, duration_ms)


def parse_file(path: str):
    with open(path, encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                yield parse_line(line)
            except InvalidLogEntry as exc:
                raise InvalidLogEntry(f"Line {line_number}: {exc}") from exc

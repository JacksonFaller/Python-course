from datetime import datetime, timezone

import pytest

from log_analyzer.parser import InvalidLogEntry, parse_line


def test_parse_line():
    entry = parse_line("2026-09-01T10:15:00Z GET /api/orders 200 31")
    assert entry.timestamp == datetime(2026, 9, 1, 10, 15, tzinfo=timezone.utc)
    assert entry.method == "GET"
    assert entry.path == "/api/orders"
    assert entry.status == 200
    assert entry.duration_ms == 31


@pytest.mark.parametrize(
    "line",
    [
        "too short",
        "2026-09-01T10:15:00Z GET /api/orders nope 31",
        "2026-09-01T10:15:00Z GET /api/orders 200 -1",
        "2026-09-01T10:15:00Z GET /api/orders 99 31",
    ],
)
def test_parse_line_rejects_invalid_input(line):
    with pytest.raises(InvalidLogEntry):
        parse_line(line)

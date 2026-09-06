from datetime import datetime, timezone

from log_analyzer.models import LogEntry
from log_analyzer.report import build_report


ENTRIES = [
    LogEntry(datetime(2026, 9, 1, tzinfo=timezone.utc), "GET", "/api/orders", 200, 31),
    LogEntry(datetime(2026, 9, 1, tzinfo=timezone.utc), "GET", "/api/orders", 500, 91),
    LogEntry(datetime(2026, 9, 1, tzinfo=timezone.utc), "GET", "/api/users", 200, 18),
    LogEntry(datetime(2026, 9, 1, tzinfo=timezone.utc), "GET", "/api/orders", 503, 144),
]


def test_build_report():
    report = build_report(ENTRIES)
    assert report["total_requests"] == 4
    assert report["by_status_class"] == {"2xx": 2, "5xx": 2}
    assert report["errors_by_path"] == {"/api/orders": 2}
    assert report["average_duration_by_path"] == {
        "/api/orders": (31 + 91 + 144) / 3,
        "/api/users": 18.0,
    }
    assert report["slowest_request"] == {
        "path": "/api/orders",
        "status": 503,
        "duration_ms": 144,
    }


def test_empty_report():
    report = build_report([])
    assert report["total_requests"] == 0
    assert report["by_status_class"] == {}
    assert report["errors_by_path"] == {}
    assert report["average_duration_by_path"] == {}
    assert report["slowest_request"] is None

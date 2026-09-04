from exercises.module02.log_report import (
    average_duration_by_path,
    build_report,
    error_count_by_path,
    failed_requests,
    slowest_request,
)


LOGS = [
    {"path": "/api/orders", "status": 200, "duration_ms": 31},
    {"path": "/api/orders", "status": 500, "duration_ms": 91},
    {"path": "/api/users", "status": 200, "duration_ms": 18},
    {"path": "/api/orders", "status": 200, "duration_ms": 42},
]


def test_failed_requests():
    assert failed_requests(LOGS) == [LOGS[1]]


def test_slowest_request():
    assert slowest_request(LOGS) == LOGS[1]


def test_average_duration_by_path():
    assert average_duration_by_path(LOGS) == {"/api/orders": 54.66666666666667, "/api/users": 18.0}


def test_error_count_by_path():
    assert error_count_by_path(LOGS) == {"/api/orders": 1, "/api/users": 0}


def test_build_report():
    report = build_report(LOGS)
    assert report["failed_requests"] == [LOGS[1]]
    assert report["slowest_request"] == LOGS[1]
    assert report["error_count_by_path"]["/api/orders"] == 1

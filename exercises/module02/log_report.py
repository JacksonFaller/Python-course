def failed_requests(logs):
    # TODO
    raise NotImplementedError


def slowest_request(logs):
    # TODO
    raise NotImplementedError


def average_duration_by_path(logs):
    # TODO
    raise NotImplementedError


def error_count_by_path(logs):
    # TODO
    raise NotImplementedError


def build_report(logs):
    # TODO: combine the operations into one useful report
    raise NotImplementedError


if __name__ == "__main__":
    logs = [
        {"path": "/api/orders", "status": 200, "duration_ms": 31},
        {"path": "/api/orders", "status": 500, "duration_ms": 91},
        {"path": "/api/users", "status": 200, "duration_ms": 18},
        {"path": "/api/orders", "status": 200, "duration_ms": 42},
    ]
    print(build_report(logs))

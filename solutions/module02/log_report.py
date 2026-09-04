from collections import defaultdict
from statistics import fmean


def failed_requests(logs):
    return [log for log in logs if log["status"] >= 500]


def slowest_request(logs):
    return max(logs, key=lambda log: log["duration_ms"])


def average_duration_by_path(logs):
    durations = defaultdict(list)
    for log in logs:
        durations[log["path"]].append(log["duration_ms"])
    return {path: fmean(values) for path, values in durations.items()}


def error_count_by_path(logs):
    counts = {log["path"]: 0 for log in logs}
    for log in logs:
        if log["status"] >= 500:
            counts[log["path"]] += 1
    return counts


def build_report(logs):
    return {
        "failed_requests": failed_requests(logs),
        "slowest_request": slowest_request(logs),
        "average_duration_by_path": average_duration_by_path(logs),
        "error_count_by_path": error_count_by_path(logs),
    }

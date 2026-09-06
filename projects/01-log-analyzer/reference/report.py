from collections import Counter, defaultdict

from log_analyzer.models import LogEntry


def build_report(entries: list[LogEntry]) -> dict:
    entries = list(entries)
    by_status = Counter(f"{entry.status // 100}xx" for entry in entries)
    errors_by_path = Counter(
        entry.path for entry in entries if entry.status >= 400
    )

    durations: dict[str, list[int]] = defaultdict(list)
    for entry in entries:
        durations[entry.path].append(entry.duration_ms)

    averages = {
        path: sum(values) / len(values)
        for path, values in durations.items()
    }
    slowest = max(entries, key=lambda entry: entry.duration_ms, default=None)

    return {
        "total_requests": len(entries),
        "by_status_class": dict(by_status),
        "errors_by_path": dict(errors_by_path),
        "average_duration_by_path": averages,
        "slowest_request": (
            {
                "path": slowest.path,
                "status": slowest.status,
                "duration_ms": slowest.duration_ms,
            }
            if slowest
            else None
        ),
    }

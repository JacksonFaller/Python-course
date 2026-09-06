from collections import Counter, defaultdict

from .models import LogEntry


def build_report(entries: list[LogEntry]) -> dict:
    entries = list(entries)

    by_status = Counter()
    errors_by_path = Counter()
    durations: dict[str, list[int]] = defaultdict(list)

    for entry in entries:
        # TODO: aggregate the status class, error count, and duration data.
        pass

    # TODO: calculate a useful report from the aggregates.
    raise NotImplementedError

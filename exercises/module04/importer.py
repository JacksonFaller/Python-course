from collections.abc import Iterable


class MalformedRecordError(ValueError):
    """A source record cannot be imported safely."""


def normalize_email(value: str) -> str:
    return value.strip().lower()


def parse_record(row: dict[str, str]) -> dict[str, str]:
    """Validate and normalize one CSV row."""
    # TODO: require name and email, then return a normalized record.
    raise NotImplementedError


def import_records(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    """Import valid rows. Invalid rows should be logged and skipped."""
    # TODO: iterate over rows and call parse_record.
    raise NotImplementedError


def group_by_email_domain(records: Iterable[dict[str, str]]) -> dict[str, int]:
    # TODO: count records by the domain part of the email address.
    raise NotImplementedError

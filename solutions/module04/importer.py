import logging
from collections import Counter
from collections.abc import Iterable

logger = logging.getLogger(__name__)


class MalformedRecordError(ValueError):
    """A source record cannot be imported safely."""


def normalize_email(value: str) -> str:
    return value.strip().lower()


def parse_record(row: dict[str, str]) -> dict[str, str]:
    name = row.get("name", "").strip()
    email = normalize_email(row.get("email", ""))
    if not name or not email or "@" not in email:
        raise MalformedRecordError("name and a valid email are required")
    return {"name": name, "email": email}


def import_records(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    imported = []
    for row in rows:
        try:
            imported.append(parse_record(row))
        except MalformedRecordError as exc:
            logger.warning("Rejected record: %s", exc)
    return imported


def group_by_email_domain(records: Iterable[dict[str, str]]) -> dict[str, int]:
    return dict(Counter(record["email"].split("@", 1)[1] for record in records))

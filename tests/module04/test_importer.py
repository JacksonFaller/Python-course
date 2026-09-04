from exercises.module04.importer import (
    MalformedRecordError,
    group_by_email_domain,
    import_records,
    parse_record,
)


def test_parse_record_normalizes_values():
    assert parse_record({"name": " Alice ", "email": "ALICE@EXAMPLE.COM"}) == {
        "name": "Alice",
        "email": "alice@example.com",
    }


def test_parse_record_rejects_missing_fields():
    try:
        parse_record({"name": "", "email": "alice@example.com"})
    except MalformedRecordError:
        pass
    else:
        raise AssertionError("Expected MalformedRecordError")


def test_import_records_skips_bad_rows():
    rows = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "", "email": "bad@example.com"},
        {"name": "Bob", "email": "bob@example.org"},
    ]
    assert import_records(rows) == [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.org"},
    ]


def test_group_by_email_domain():
    records = [
        {"name": "A", "email": "a@example.com"},
        {"name": "B", "email": "b@example.org"},
        {"name": "C", "email": "c@example.com"},
    ]
    assert group_by_email_domain(records) == {"example.com": 2, "example.org": 1}

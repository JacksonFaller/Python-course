import pytest

from exercises.module09.string_parser import InvalidToken, parse_token


@pytest.mark.parametrize(
    ("value", "expected"),
    [("alpha:10", ("alpha", 10)), ("job:42", ("job", 42))],
)
def test_parse_token(value, expected):
    assert parse_token(value) == expected


@pytest.mark.parametrize("value", ["", ":10", "alpha:", "alpha:nope"])
def test_invalid_token(value):
    with pytest.raises(InvalidToken):
        parse_token(value)

class InvalidToken(ValueError):
    pass


def parse_token(value: str) -> tuple[str, int]:
    name, separator, number = value.partition(":")
    if not separator or not name or not number:
        raise InvalidToken(value)
    try:
        parsed = int(number)
    except ValueError as exc:
        raise InvalidToken(value) from exc
    return name, parsed

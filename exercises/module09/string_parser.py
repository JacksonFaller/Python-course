class InvalidToken(ValueError):
    pass


def parse_token(value: str) -> tuple[str, int]:
    # Expected format: NAME:NUMBER
    # TODO: validate and return the two parts.
    raise NotImplementedError

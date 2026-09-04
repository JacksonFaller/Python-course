from exercises.module01.config import normalize_config


def test_defaults_are_applied():
    assert normalize_config({}) == {"host": "localhost", "port": 8080, "debug": False}


def test_existing_values_are_preserved():
    assert normalize_config({"host": "api", "port": 9000, "debug": True}) == {
        "host": "api",
        "port": 9000,
        "debug": True,
    }

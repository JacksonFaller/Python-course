def normalize_config(config):
    # TODO: fill missing values with the defaults described in exercises.md
    raise NotImplementedError


if __name__ == "__main__":
    print(normalize_config({}))
    print(normalize_config({"host": "api.internal", "debug": True}))

def normalize_config(config):
    return {
        "host": config.get("host", "localhost"),
        "port": config.get("port", 8080),
        "debug": config.get("debug", False),
    }

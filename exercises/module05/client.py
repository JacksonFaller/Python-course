from pathlib import Path
from typing import Any


class ApiSnapshotClient:
    def __init__(self, timeout: float = 10.0) -> None:
        self.timeout = timeout

    def fetch_json(self, url: str) -> Any:
        # TODO: perform a GET request, raise for HTTP errors, return JSON.
        raise NotImplementedError

    def save_json(self, data: Any, output: Path) -> None:
        # TODO: create the parent directory and save indented JSON.
        raise NotImplementedError

import json
from pathlib import Path
from typing import Any

import httpx


class ApiSnapshotClient:
    def __init__(self, timeout: float = 10.0) -> None:
        self.timeout = timeout

    def fetch_json(self, url: str) -> Any:
        response = httpx.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def save_json(self, data: Any, output: Path) -> None:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

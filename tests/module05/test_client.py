from pathlib import Path

from exercises.module05.client import ApiSnapshotClient


def test_save_json_creates_parent_directories(tmp_path: Path):
    client = ApiSnapshotClient()
    output = tmp_path / "nested" / "snapshot.json"
    client.save_json({"ok": True, "items": [1, 2]}, output)
    assert output.exists()
    assert '"ok": true' in output.read_text(encoding="utf-8")


def test_fetch_json_uses_http_client(monkeypatch):
    class Response:
        def raise_for_status(self):
            pass

        def json(self):
            return {"value": 42}

    def fake_get(url, timeout):
        assert url == "https://example.test/data"
        assert timeout == 3.5
        return Response()

    monkeypatch.setattr("exercises.module05.client.httpx.get", fake_get)
    assert ApiSnapshotClient(timeout=3.5).fetch_json("https://example.test/data") == {"value": 42}

from fastapi.testclient import TestClient

from inventory_api.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_products_endpoint_is_not_implemented_yet():
    response = client.get("/products")
    assert response.status_code == 404

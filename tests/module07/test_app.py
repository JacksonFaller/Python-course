from fastapi.testclient import TestClient

from exercises.module07.app import app, _products


client = TestClient(app)


def setup_function():
    _products.clear()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_product():
    created = client.post("/products", json={"sku": "A-1", "name": "Keyboard", "quantity": 5})
    assert created.status_code == 201
    assert client.get("/products/A-1").json()["quantity"] == 5


def test_unknown_product_is_404():
    assert client.get("/products/NOPE").status_code == 404


def test_quantity_cannot_be_negative():
    response = client.post("/products", json={"sku": "A-1", "name": "Keyboard", "quantity": 5})
    assert response.status_code == 201
    assert client.patch("/products/A-1/quantity?quantity=-1").status_code == 422

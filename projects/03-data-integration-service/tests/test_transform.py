import pytest

from integration_service.transform import transform_product


def test_transform_product():
    product = transform_product(
        {"id": "p-42", "name": " Keyboard ", "price": 49.5}
    )
    assert product.external_id == "p-42"
    assert product.name == "Keyboard"
    assert product.price == 49.5


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"id": "p-1", "name": "Keyboard"},
        {"id": "p-1", "name": "Keyboard", "price": -1},
    ],
)
def test_transform_product_rejects_invalid_payload(payload):
    with pytest.raises(ValueError):
        transform_product(payload)

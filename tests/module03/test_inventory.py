import pytest

from exercises.module03.inventory import InsufficientStockError, Product, Warehouse


def test_receive_increases_quantity():
    product = Product("KB-001", "Keyboard")
    product.receive(10)
    assert product.quantity == 10


def test_reserve_decreases_quantity():
    product = Product("KB-001", "Keyboard", 10)
    product.reserve(3)
    assert product.quantity == 7


def test_reserve_too_much_raises():
    product = Product("KB-001", "Keyboard", 2)
    with pytest.raises(InsufficientStockError):
        product.reserve(3)


def test_warehouse_lookup():
    warehouse = Warehouse()
    warehouse.add(Product("KB-001", "Keyboard"))
    assert warehouse.get("KB-001").sku == "KB-001"


def test_warehouse_unknown_sku_is_an_error():
    warehouse = Warehouse()
    with pytest.raises(KeyError):
        warehouse.get("missing")


def test_duplicate_sku_is_an_error():
    warehouse = Warehouse()
    warehouse.add(Product("KB-001", "Keyboard"))
    with pytest.raises(ValueError):
        warehouse.add(Product("KB-001", "Another keyboard"))

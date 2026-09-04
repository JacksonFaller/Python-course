from exercises.module01.customer_lookup import (
    active_customer_names,
    customer_names_by_id,
    find_customer,
)


def test_active_customer_names():
    customers = [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "Bob", "active": False},
        {"id": 3, "name": "Carol", "active": True},
    ]
    assert active_customer_names(customers) == ["Alice", "Carol"]


def test_find_customer_returns_none_when_missing():
    assert find_customer([], 999) is None


def test_customer_names_by_id():
    customers = [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "Bob", "active": False},
    ]
    assert customer_names_by_id(customers) == {1: "Alice", 2: "Bob"}

from collections import defaultdict


customers = [
    {"id": 1, "name": "Alice", "active": True},
    {"id": 2, "name": "Bob", "active": False},
    {"id": 3, "name": "Carol", "active": True},
]


def active_customer_names(customers):
    return [customer["name"] for customer in customers if customer["active"]]


def find_customer(customers, customer_id):
    return next((customer for customer in customers if customer["id"] == customer_id), None)


def customer_names_by_id(customers):
    return {customer["id"]: customer["name"] for customer in customers}


def normalize_config(config):
    return {
        "host": config.get("host", "localhost"),
        "port": config.get("port", 8080),
        "debug": config.get("debug", False),
    }


def summarize_paid_orders(orders):
    summary = defaultdict(lambda: {"count": 0, "total": 0.0})

    for order in orders:
        if order["status"] != "paid":
            continue

        customer = order["customer"]
        summary[customer]["count"] += 1
        summary[customer]["total"] += order["total"]

    return dict(summary)


if __name__ == "__main__":
    orders = [
        {"id": 101, "customer": "alice", "total": 120.50, "status": "paid"},
        {"id": 102, "customer": "bob", "total": 80.00, "status": "pending"},
        {"id": 103, "customer": "alice", "total": 45.25, "status": "paid"},
        {"id": 104, "customer": "bob", "total": 30.00, "status": "cancelled"},
    ]

    assert active_customer_names(customers) == ["Alice", "Carol"]
    assert find_customer(customers, 2)["name"] == "Bob"
    assert find_customer(customers, 999) is None
    assert customer_names_by_id(customers) == {1: "Alice", 2: "Bob", 3: "Carol"}
    assert normalize_config({}) == {"host": "localhost", "port": 8080, "debug": False}
    assert summarize_paid_orders(orders) == {
        "alice": {"count": 2, "total": 165.75}
    }

    print("All checks passed.")

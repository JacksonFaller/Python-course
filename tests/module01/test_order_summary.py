from exercises.module01.order_summary import summarize_paid_orders


ORDERS = [
    {"id": 101, "customer": "alice", "total": 120.50, "status": "paid"},
    {"id": 102, "customer": "bob", "total": 80.00, "status": "pending"},
    {"id": 103, "customer": "alice", "total": 45.25, "status": "paid"},
    {"id": 104, "customer": "bob", "total": 30.00, "status": "cancelled"},
]


def test_paid_orders_are_grouped_and_summed():
    assert summarize_paid_orders(ORDERS) == {"alice": {"count": 2, "total": 165.75}}


def test_empty_input():
    assert summarize_paid_orders([]) == {}


def test_unpaid_customer_is_excluded():
    assert summarize_paid_orders(ORDERS[1:2]) == {}

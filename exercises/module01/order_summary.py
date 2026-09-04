def summarize_paid_orders(orders):
    # TODO: return {customer: {"count": int, "total": float}}
    # Include only customers with at least one paid order.
    raise NotImplementedError


if __name__ == "__main__":
    orders = [
        {"id": 101, "customer": "alice", "total": 120.50, "status": "paid"},
        {"id": 102, "customer": "bob", "total": 80.00, "status": "pending"},
        {"id": 103, "customer": "alice", "total": 45.25, "status": "paid"},
        {"id": 104, "customer": "bob", "total": 30.00, "status": "cancelled"},
    ]
    print(summarize_paid_orders(orders))

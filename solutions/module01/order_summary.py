from collections import defaultdict


def summarize_paid_orders(orders):
    summary = defaultdict(lambda: {"count": 0, "total": 0.0})
    for order in orders:
        if order["status"] != "paid":
            continue
        customer = order["customer"]
        summary[customer]["count"] += 1
        summary[customer]["total"] += order["total"]
    return dict(summary)

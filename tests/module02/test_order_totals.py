from exercises.module02.order_totals import calculate_total


def test_calculate_total():
    order = {
        "items": [
            {"price": 80.0, "quantity": 2},
            {"price": 25.0, "quantity": 1},
        ]
    }
    assert calculate_total(order) == 185.0

def calculate_total(order):
    # TODO: sum item price * quantity
    raise NotImplementedError


if __name__ == "__main__":
    order = {
        "items": [
            {"name": "Keyboard", "price": 80.0, "quantity": 2},
            {"name": "Mouse", "price": 25.0, "quantity": 1},
        ]
    }
    print(calculate_total(order))

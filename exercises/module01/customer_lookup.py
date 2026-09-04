customers = [
    {"id": 1, "name": "Alice", "active": True},
    {"id": 2, "name": "Bob", "active": False},
    {"id": 3, "name": "Carol", "active": True},
]


def active_customer_names(customers):
    # TODO: return the names of active customers
    raise NotImplementedError


def find_customer(customers, customer_id):
    # TODO: return the matching customer, or None
    raise NotImplementedError


def customer_names_by_id(customers):
    # TODO: return {customer_id: name}
    raise NotImplementedError


if __name__ == "__main__":
    print(active_customer_names(customers))
    print(find_customer(customers, 2))
    print(customer_names_by_id(customers))

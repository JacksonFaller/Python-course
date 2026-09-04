def active_customer_names(customers):
    return [customer["name"] for customer in customers if customer["active"]]


def find_customer(customers, customer_id):
    return next((customer for customer in customers if customer["id"] == customer_id), None)


def customer_names_by_id(customers):
    return {customer["id"]: customer["name"] for customer in customers}

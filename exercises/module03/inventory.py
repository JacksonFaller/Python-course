from dataclasses import dataclass


@dataclass
class Product:
    sku: str
    name: str
    quantity: int = 0

    def receive(self, amount: int) -> None:
        # TODO
        raise NotImplementedError

    def reserve(self, amount: int) -> None:
        # TODO
        raise NotImplementedError


class InsufficientStockError(Exception):
    pass


class Warehouse:
    def __init__(self) -> None:
        self._products = {}

    def add(self, product: Product) -> None:
        # TODO
        raise NotImplementedError

    def get(self, sku: str) -> Product:
        # TODO
        raise NotImplementedError

    def receive(self, sku: str, amount: int) -> None:
        # TODO
        raise NotImplementedError

    def reserve(self, sku: str, amount: int) -> None:
        # TODO
        raise NotImplementedError


if __name__ == "__main__":
    warehouse = Warehouse()
    warehouse.add(Product("KB-001", "Keyboard"))
    warehouse.receive("KB-001", 10)
    warehouse.reserve("KB-001", 3)
    print(warehouse.get("KB-001"))

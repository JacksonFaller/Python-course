from dataclasses import dataclass


class InsufficientStockError(Exception):
    pass


@dataclass
class Product:
    sku: str
    name: str
    quantity: int = 0

    def receive(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Quantity must be positive")
        self.quantity += amount

    def reserve(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Quantity must be positive")
        if amount > self.quantity:
            raise InsufficientStockError(f"Not enough stock for {self.sku}")
        self.quantity -= amount


class Warehouse:
    def __init__(self) -> None:
        self._products = {}

    def add(self, product: Product) -> None:
        if product.sku in self._products:
            raise ValueError(f"SKU already exists: {product.sku}")
        self._products[product.sku] = product

    def get(self, sku: str) -> Product:
        return self._products[sku]

    def receive(self, sku: str, amount: int) -> None:
        self.get(sku).receive(amount)

    def reserve(self, sku: str, amount: int) -> None:
        self.get(sku).reserve(amount)

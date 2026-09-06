from dataclasses import dataclass


@dataclass(frozen=True)
class ExternalProduct:
    external_id: str
    name: str
    price: float


@dataclass(frozen=True)
class Product:
    external_id: str
    name: str
    price: float

from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    sku: Mapped[str] = mapped_column(String(40), primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    quantity: Mapped[int] = mapped_column(default=0)


def create_database(url: str = "sqlite://"):
    # TODO: create the engine and schema, then return the engine.
    raise NotImplementedError


class ProductRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, product: Product) -> None:
        # TODO
        raise NotImplementedError

    def get(self, sku: str) -> Product | None:
        # TODO
        raise NotImplementedError

    def set_quantity(self, sku: str, quantity: int) -> None:
        # TODO: update a known product and persist the change.
        raise NotImplementedError

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
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    return engine


class ProductRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, product: Product) -> None:
        self.session.add(product)
        self.session.commit()

    def get(self, sku: str) -> Product | None:
        return self.session.scalar(select(Product).where(Product.sku == sku))

    def set_quantity(self, sku: str, quantity: int) -> None:
        product = self.get(sku)
        if product is None:
            raise KeyError(sku)
        product.quantity = quantity
        self.session.commit()

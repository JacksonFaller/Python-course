from sqlalchemy.orm import Session

from exercises.module06.repository import Product, ProductRepository, create_database


def test_add_and_get():
    engine = create_database()
    with Session(engine) as session:
        repo = ProductRepository(session)
        repo.add(Product(sku="A-1", name="Keyboard", quantity=5))

    with Session(engine) as session:
        product = ProductRepository(session).get("A-1")
        assert product is not None
        assert product.quantity == 5


def test_set_quantity_persists():
    engine = create_database()
    with Session(engine) as session:
        repo = ProductRepository(session)
        repo.add(Product(sku="A-1", name="Keyboard", quantity=5))
        repo.set_quantity("A-1", 11)

    with Session(engine) as session:
        assert ProductRepository(session).get("A-1").quantity == 11

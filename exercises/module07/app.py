from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class ProductCreate(BaseModel):
    sku: str
    name: str
    quantity: int = 0


class ProductOut(ProductCreate):
    pass


app = FastAPI(title="Inventory API")
_products: dict[str, ProductOut] = {}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/products/{sku}", response_model=ProductOut)
def get_product(sku: str) -> ProductOut:
    # TODO
    raise NotImplementedError


@app.post("/products", response_model=ProductOut, status_code=201)
def create_product(product: ProductCreate) -> ProductOut:
    # TODO
    raise NotImplementedError


@app.patch("/products/{sku}/quantity", response_model=ProductOut)
def set_quantity(sku: str, quantity: int) -> ProductOut:
    # TODO
    raise NotImplementedError

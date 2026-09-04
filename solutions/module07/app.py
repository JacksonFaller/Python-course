from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    sku: str
    name: str
    quantity: int = Field(default=0, ge=0)


class ProductOut(ProductCreate):
    pass


app = FastAPI(title="Inventory API")
_products: dict[str, ProductOut] = {}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/products/{sku}", response_model=ProductOut)
def get_product(sku: str) -> ProductOut:
    product = _products.get(sku)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/products", response_model=ProductOut, status_code=201)
def create_product(product: ProductCreate) -> ProductOut:
    if product.sku in _products:
        raise HTTPException(status_code=409, detail="Product already exists")
    saved = ProductOut.model_validate(product)
    _products[saved.sku] = saved
    return saved


@app.patch("/products/{sku}/quantity", response_model=ProductOut)
def set_quantity(sku: str, quantity: int) -> ProductOut:
    if quantity < 0:
        raise HTTPException(status_code=422, detail="Quantity cannot be negative")
    product = _products.get(sku)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    product.quantity = quantity
    return product

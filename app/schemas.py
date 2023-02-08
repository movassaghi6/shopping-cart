from datetime import datetime
from pydantic import BaseModel


class ProductBase(BaseModel):
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UpdateProduct(ProductBase):
    id: int
    updated_at: datetime | None = None

    class Config:
        orm_mode = True


class CartBase(BaseModel):
    id: int


class CartCreate(CartBase):
    pass


class Cart(CartBase):
    id: int
    products: list[Product] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

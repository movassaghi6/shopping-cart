from sqlalchemy.orm import Session
from fastapi import status, Response

from . import models, schemas


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_cart_product(db: Session, product: schemas.ProductCreate, cart_id: int):
    db_product = models.Product(**product.dict(), owner_id = cart_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(id: int, product: schemas.UpdateProduct, db: Session):
    product_query = db.query(models.Product).filter(models.Product.id == id)
    updated_product = product_query.first()
    product.id = id
    product_query.update(product.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return updated_product


def get_product(db: Session, id: int):
    return db.query(models.Product).filter(models.Product.id == id).first()


def delete_product(id: int, db: Session):
    product_query= db.query(models.Product).filter(models.Product.id == id)
    product = product_query.first()
    product_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def get_cart(db: Session, cart_id: int):
    return db.query(models.Cart).filter(models.Cart.id == cart_id).first()


def get_carts(db: Session, skip: int =0, limit: int = 100):
    return db.query(models.Cart).offset(skip).limit(limit).all()


def create_cart(db: Session, cart: schemas.CartCreate):
    db_cart = models.Cart(**cart.dict())
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

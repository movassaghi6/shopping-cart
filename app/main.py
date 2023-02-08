from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/carts/", response_model=schemas.Cart)
def create_cart(cart: schemas.CartCreate, db: Session = Depends(get_db)):
    db_cart = crud.get_cart(db, cart_id=cart.id)
    if db_cart:
        raise HTTPException(status_code=400, detail="cart with this id is already used.")
    return crud.create_cart(db=db, cart=cart)


@app.get("/carts/", response_model=list[schemas.Cart])
def read_carts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    carts = crud.get_carts(db, skip=skip, limit=limit)
    return carts


@app.get("/carts/{cart_id}", response_model=schemas.Cart)
def read_cart(cart_id: int, db: Session = Depends(get_db)):
    db_cart = crud.get_cart(db, cart_id= cart_id)
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    return db_cart


@app.post("/carts/{cart_id}/products/", response_model=schemas.Product)
def create_product_for_cart(
    cart_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)
):
    return crud.create_cart_product(db = db, product=product, cart_id=cart_id)


@app.get("/products/", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.get("/products/{id}", response_model=schemas.Product)
def read_product(id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, id=id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@app.put("/products/{id}", response_model=schemas.Product)
def update_product(id: int, product: schemas.UpdateProduct, db: Session = Depends(get_db)):
    return crud.update_product(db= db ,product=product, id=id)


@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db= db, id=id)


@app.get('/api/healthchecker')
def root():
    return {'message': 'Hello World'}
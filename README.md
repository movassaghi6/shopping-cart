# shopping-cart
> a CRUD RESTful API with Python, FastAPI, SQLAlchemy ORM, Pydantic, PostgreSQL, and Docker-compose
## Introduction

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

The key features that I like in FastApi are:

* **Fast to code**: Increase the speed to develop features by about 200% to 300%. *
* **Fewer bugs**: Reduce about 40% of human (developer) induced errors. *
* **Easy**: Designed to be easy to use and learn. Less time reading docs.
* **Robust**: Get production-ready code. With automatic interactive documentation.
* **Standards-based**: Based on (and fully compatible with) the open standards for APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (previously known as Swagger) and <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.



## Getting Started

To get started make sure the following requirements (for development and deployment tooling) are installed on your system:

- [Python 3.11+](https://www.python.org/downloads/) (Project Programming Language)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) (Python Dependency Manager)
- [Docker](https://hub.docker.com/) (Containerization)
- [Docker Compose](https://docs.docker.com/compose/) (Composer for Docker)

To getting started with deployment:

1.You have to implement .env file in the root of project but what is the structure of this file:
```
# These credentials will be used by the Postgres Docker image to configure the PostgreSQL database.
DATABASE_PORT=6500
POSTGRES_PASSWORD=examplepassword
POSTGRES_USER=exampleusername
POSTGRES_DB=examplename
POSTGRES_HOST=examplehostname
POSTGRES_HOSTNAME=127.0.0.1
```

2.run following command to build docker image and start container:
```
docker-compose up -d
```
3.create python virtualenv
```
python3 -m venv venv
```
4.active python virtualenv

5.install packages
```
pip install -r requirements.txt
```
6.run project
```
uvicorn main:app --reload
```
7. now go to:
```
http://localhost:8000/docs
```



## Endpoints

A basic shopping cart application has features such as  Cart functionalities and Admin CRUD capabilities among other functionalities.

We have the following API's:
![Swagger UI](https://github.com/movassaghi6/shopping-cart/blob/main/screenshot.png)

## A few assumptions
You have a good understanding of Python Language
The project you want to use this codebase for uses an SQL Database
You have an understanding of sqlalchemy as an ORM
The Repository contains 5 main files namely:

#### main.py
This file is the entry point for the application. It contains the main routes and redirects all requested routes to their respective functions.
#### crud.py
This file contains the main functions that interact with the database, it is basically where the business logic happens.
#### models.py
This file is similar to the one in Django. In this file is where we define our database tables.
#### schemas.py
This file contains the data schemas for our application.
#### database.py
This file contains our database connection string.


## Code Samples
Just to show you how the flow works here is the working example of the get_item/id endpoint.
#### main.py
```
@app.get("/carts/{cart_id}", response_model=schemas.Cart)
def read_cart(cart_id: int, db: Session = Depends(get_db)):
    db_cart = crud.get_cart(db, cart_id= cart_id)
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    return db_cart
```
The above piece of code handles the endpoint and calls the function get_item_by_id in the crud.py file for further processing.
#### crud.py
```
def get_cart(db: Session, cart_id: int):
    return db.query(models.Cart).filter(models.Cart.id == cart_id).first()
```
The above piece of code handles the get_cart call and queries the DB for an item with the id passed in the parameter.


## Todo

- Add support for user registeration and logging
- add testing
- Implement better error handling
- Implement incomplete endpoints

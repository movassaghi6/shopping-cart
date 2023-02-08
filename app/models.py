from sqlalchemy import Column, ForeignKey, String, Integer, text, TIMESTAMP, Float
from sqlalchemy.orm import relationship

from .database import Base

class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, nullable=False, primary_key=True, index=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))

    products = relationship("Product", back_populates="owner")

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, nullable=False, primary_key=True, index=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    image = Column(String, nullable=True)
    rating = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    owner_id = Column(Integer, ForeignKey("carts.id"))

    owner = relationship("Cart", back_populates="products")
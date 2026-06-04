from sqlalchemy import Column, Integer, String, Float, ForeignKey,Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    product_id = Column(String(20), unique=True, nullable=False)

    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="products")
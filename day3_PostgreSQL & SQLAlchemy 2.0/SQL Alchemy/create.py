from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)
from sqlalchemy.orm import declarative_base, relationship, validates
import re

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    # One User -> Many Products
    products = relationship("Product", back_populates="user")

    @validates("email")
    def validate_email(self, key, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.match(pattern, email):
            raise ValueError("Invalid email format")

        return email

    @validates("password")
    def validate_password(self, key, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if not re.search(r"[A-Z]", password):
            raise ValueError(
                "Password must contain at least one uppercase letter"
            )

        if not re.search(r"[a-z]", password):
            raise ValueError(
                "Password must contain at least one lowercase letter"
            )

        if not re.search(r"\d", password):
            raise ValueError(
                "Password must contain at least one digit"
            )

        if not re.search(r"[@$!%*?&]", password):
            raise ValueError(
                "Password must contain at least one special character"
            )

        return password


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    product_id = Column(
        String(20),
        unique=True,
        nullable=False
    )

    name = Column(String(100), nullable=False)

    price = Column(Float, nullable=False)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    # Many Products -> One User
    user = relationship("User", back_populates="products")


# Database Connection
engine = create_engine(
    "postgresql://postgres:Welcome%402826@localhost:5432/fastapi_db"
)

# Create Tables
Base.metadata.create_all(engine)

print("Users and Products tables created successfully")
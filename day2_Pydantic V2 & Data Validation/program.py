# pydantic basemodel
from pydantic import BaseModel
class User(BaseModel):
    age: int

user = User(age="abc")
print(user) 

# Automatic Type Conversion
from pydantic import BaseModel
class User(BaseModel):
    age: int
    salary: float
    active: bool

user = User(
    age="25",
    salary="50000",
    active="true"
)
print(user) 

# Min_length 
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(
        ...,
        min_length=3
    )
User(username="john")
User(username="ab")

# Max_length
class User(BaseModel):
    username: str = Field(
        ...,
        max_length=20
    )
User(username="john_doe")
User(username="a"*21)

# min_length and max_length
class User(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=20
    )
User(username="john_doe")
User(username="ab")

# ge (Greater Than or Equal)
class Product(BaseModel):
    price: float = Field(
        ...,
        ge=0
    )
Product(price=19.99)
Product(price=-5)   

# le (Less Than or Equal)
class Product(BaseModel):
    price: float = Field(
        ...,
        le=1000
    )

Product(price=19.99)
Product(price=1500)

# gt (Greater Than)
class Product(BaseModel):
    price: float = Field(
        ...,
        gt=0
    )
Product(price=19.99)
Product(price=0)

# lt (Less Than)
class Product(BaseModel):
    price: float = Field(
        ...,
        lt=1000
    )
Product(price=19.99)
Product(price=1000)

# pattern
from pydantic import BaseModel, Field
class User(BaseModel):
    name: str = Field(
        ...,
        pattern=r"^[A-Za-z]+$"
    )
User(name="John")
User(name="John123")
print(user)
print(user)

# min_length, max_length, ge, le, pattern
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=20
    )

    email: str = Field(
        ...,
        min_length=5,
        max_length=100
    )

    age: int = Field(
        ...,
        ge=18,
        le=100
    )

    phone: str = Field(
        ...,
        pattern=r"^[6-9]\d{9}$"
    )

user = UserCreate(
    username="jabir",
    email="jabir@gmail.com",
    age=25,
    phone="9876543210"
)

print(user)


# Field Validators
# Username Validator
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str

    @field_validator("username")
    @classmethod
    def username_validator(cls, value):
        if len(value) < 5:
            raise ValueError(
                "Username must be at least 5 characters"
            )
        return value
# input 
user = User(username="jabir123")

print(user)

# Validating Multiple Fields
from pydantic import BaseModel, field_validator

class User(BaseModel):
    first_name: str
    last_name: str

    @field_validator(
        "first_name",
        "last_name"
    )
    @classmethod
    def validate_names(cls, value):
        if len(value) < 2:
            raise ValueError(
                "Name too short"
            )
        return value
    
User(email="test@hotmail.com")

# Email Validator
from pydantic import BaseModel, field_validator

class User(BaseModel):
    email: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):

        allowed_domains = [
            "gmail.com",
            "yahoo.com"
        ]

        domain = value.split("@")[-1]

        if domain not in allowed_domains:
            raise ValueError(
                "Only Gmail and Yahoo allowed"
            )

        return value
    
user = User(email="jabir@gmail.com")
print(user)

# Validation Modes
# Mode = "before"
from pydantic import BaseModel, field_validator

class User(BaseModel):
    age: int

    @field_validator("age", mode="before")
    @classmethod
    def convert_age(cls, value):
        return int(value)
User(age="25")
print(user)

# Mode = "after"
from pydantic import BaseModel, field_validator
class User(BaseModel):
    age: int

    @field_validator("age", mode="after")
    @classmethod
    def check_age(cls, value):
        if value < 18:
            raise ValueError(
                "Age must be at least 18"
            )
        return value
User(age=25)
print(user)

# Model Validators
from pydantic import BaseModel, model_validator
class User(BaseModel):

    password: str
    confirm_password: str

    @model_validator(mode="after")
    def validate_passwords(self):

        if self.password != self.confirm_password:
            raise ValueError(
                "Passwords do not match"
            )

        return self
user = User(
    password="secret123",
    confirm_password="secret123"
)
print(user)

# Date Validation
from datetime import date
from pydantic import BaseModel, model_validator

class Event(BaseModel):
    start_date: date
    end_date: date

    @model_validator(mode="after")
    def validate_dates(self):

        if self.end_date < self.start_date:
            raise ValueError(
                "End date must be after start date"
            )

        return self
event = Event(
    start_date="2024-01-01",
    end_date="2024-01-10"
)   

# Nested Model 
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

# input 
user = User(
    id=1,
    name="John",
    address={
        "street": "123 Main St",
        "city": "New York",
        "zip_code": "10001"
    }
)

print(user)

# multi-level nested model
from pydantic import BaseModel

class Country(BaseModel):
    name: str
    code: str

class Address(BaseModel):
    street: str
    city: str
    country: Country

class User(BaseModel):
    id: int
    name: str
    address: Address

#input 
user = User(
    id=1,
    name="John",
    address={
        "street": "Main Street",
        "city": "New York",
        "country": {
            "name": "United States",
            "code": "US"
        }
    }
)
print(user)

# List of Nested Models
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name: str
    addresses: list[Address]

# input
user = User(
    name="John",
    addresses=[
        {
            "city": "New York",
            "country": "USA"
        },
        {
            "city": "London",
            "country": "UK"
        }
    ]
)
print(user)

# Optional Nested Models
from typing import Optional
from pydantic import BaseModel

class Address(BaseModel):
    city: str

class User(BaseModel):
    name: str
    address: Optional[Address] = None

# input 
User(
    name="John",
    address={"city": "New York"}
)

# Nested Models with Field Validation
from pydantic import BaseModel, Field

class Review(BaseModel):
    rating: int = Field(
        ge=1,
        le=5
    )

class Product(BaseModel):
    name: str
    review: Review

# input
product = Product(
    name="Laptop",
    review={
        "rating": 4
    }
)
print(product)

# Required Field
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str

# input
{
    "username": "john",
    "email": "john@gmail.com"
}

# Optional Field
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    username: str
    phone: Optional[str] = None

# input
User(
    username="john",
    phone="9876543210"
)


# Default Values Make Fields Optional
class Product(BaseModel):
    name: str
    stock: int = 0
# input
Product(name="Laptop")


# User Registration Schema
from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):

    username: str
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "jabir123",
                "email": "jabir@gmail.com",
                "password": "StrongPass123"
            }
        }
    )

# Product Creation API
from pydantic import BaseModel, ConfigDict

class ProductCreate(BaseModel):

    name: str
    price: float
    stock: int

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Laptop",
                "price": 75000.50,
                "stock": 20
            }
        }
    )


# from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict

app = FastAPI()

class UserCreate(BaseModel):

    username: str
    email: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "jabir123",
                "email": "jabir@gmail.com"
            }
        }
    )

@app.post("/users")
def create_user(user: UserCreate):
    return user
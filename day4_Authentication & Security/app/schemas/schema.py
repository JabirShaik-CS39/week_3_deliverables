from pydantic import BaseModel, EmailStr

# USER
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


# PRODUCT
class ProductCreate(BaseModel):
    product_id: int
    name: str
    price: float
    user_id: int


class ProductResponse(BaseModel):
    id: int
    product_id: int
    name: str
    price: float
    user_id: int

    class Config:
        from_attributes = True
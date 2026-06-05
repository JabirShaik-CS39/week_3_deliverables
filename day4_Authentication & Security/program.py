# Authentication Endpoints
# register new user
# Example Request
# POST /register

{
    "email": "admin@gmail.com",
    "password": "Admin@123"
}
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .database import get_db
from .models import User
from .schemas import UserCreate
router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    hashed_password = pwd_context.hash(user.password)

    db_user = User(
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(db_user)
    db.commit()

    return {"message": "User registered successfully"}


# login
from fastapi.security import OAuth2PasswordRequestForm
from .auth import authenticate_user, create_access_token, create_refresh_token

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    user = authenticate_user(
        form_data.username,
        form_data.password
    )

    access_token = create_access_token(
        data={"sub": user.email}
    )

    refresh_token = create_refresh_token(
        data={"sub": user.email}
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


# me

#Response
{
    "id": 1,
    "email": "admin@gmail.com"
}
# Example

from .auth import get_current_user

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return current_user



# refresh
from .auth import verify_token

@router.post("/refresh")
def refresh_token(refresh_token: str):

    payload = verify_token(refresh_token)

    new_access_token = create_access_token(
        {"sub": payload["sub"]}
    )

    return {
        "access_token": new_access_token
    }


## Route Protection with Depends()
# OAuth2PasswordBearer

from fastapi.security import OAuth2PasswordBearer
from .auth import verify_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

# Current User Dependency
def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    return payload

# Protected Route
from fastapi import HTTPException, status
from jose import JWTError, jwt
from .auth import SECRET_KEY, ALGORITHM
from .auth import get_current_user
import app
@app.get("/profile")
def profile(
    current_user=Depends(get_current_user)
):
    return current_user


##Environment Variables using Pydantic Settings

# settings.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()

# Usage 
from settings import settings

SECRET_KEY = settings.SECRET_KEY


## Secure Product APIs
# Public Route
from fastapi import FastAPI
app = FastAPI()
from app import products

@app.get("/products")
def get_products():
    return products

#Admin Create Product
from .auth import get_current_user
from app import products
from .auth import admin_required
from app.schemas import ProductCreate

@app.post("/products")
def create_product(
    product: ProductCreate,
    admin=Depends(admin_required)
):
    return {
        "message": "Product created"
    }


# Admin Update Product
import app
from app.schemas import ProductUpdate
@app.put("/products/{id}")
def update_product(
    id: int,
    product: ProductUpdate,
    admin=Depends(admin_required)
):
    return {
        "message": "Product updated"
    }

# Admin Delete Product

@app.delete("/products/{id}")
def delete_product(
    id: int,
    admin=Depends(admin_required)
):
    return {
        "message": "Deleted"
    }
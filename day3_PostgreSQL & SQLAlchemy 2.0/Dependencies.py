# Basic Dependency Injection with FastAPI

from fastapi import FastAPI, Depends

app = FastAPI()

def common_parameters(q: str = None, limit: int = 10):
    return {"q": q, "limit": limit}

@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    return commons


# Database Dependency #?
from sqlalchemy.orm import Session
from fastapi import Depends
from database import SessionLocal

# Dependency function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Authentication Dependency Example

from fastapi import Depends, HTTPException

def get_current_user(token: str):
    if token != "valid_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user_id": 1}

@app.get("/profile")
def profile(user: dict = Depends(get_current_user)):
    return user


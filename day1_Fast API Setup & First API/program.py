# create user schema
from pydantic import BaseModel

class UserCreate(BaseModel):
    id : int
    name: str
    email: str


# First GET Endpoint
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


# Multiple GET Endpoints
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Home Page"}

@app.get("/about")
def about():
    return {"message": "About Page"}

@app.get("/contact")
def contact():
    return {"message": "Contact Page"}


# Path Parameters

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id):
    return {"user_id": user_id}

# type conversion

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


# Path Parameters and CRUD Operations
#Read a User

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"message": f"Fetching user {user_id}"}

# Update a User

@app.put("/users/{user_id}")
def update_user(user_id: int):
    return {"message": f"Updating user {user_id}"}


# Delete a User

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"message": f"Deleting user {user_id}"}


# path validation

from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(
    user_id: int = Path(
        gt=0,
        lt=1000,
        description="User ID must be between 1 and 999"
    )
):
    return {"user_id": user_id}


# Query Parameters

from fastapi import FastAPI
app = FastAPI()

@app.get("/search")
def search_item(keyword: str):
    return {"keyword": keyword}


# Multiple Query Parameters

from fastapi import FastAPI
app = FastAPI()

@app.get("/products")
def get_products(
    category: str,
    page: int
):
    return {
        "category": category,
        "page": page
    }


# Request Body
# Create a Model

from pydantic import BaseModel
class Student(BaseModel):
    name: str
    age: int
    course: str

# Create a POST Endpoint
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    course: str

@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created",
        "student": student
    }


# from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

app = FastAPI()

class Address(BaseModel):
    city: str
    state: str

class User(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=18)
    email: EmailStr
    phone: Optional[str] = None
    skills: List[str]
    address: Address

@app.post("/users")
def create_user(user: User):
    return {
        "message": "User Created",
        "data": user.model_dump()
    }



# Response Models

# Create a Pydantic Model
from pydantic import BaseModel
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

# Use response_model
from fastapi import FastAPI

app = FastAPI()

@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "id": 1,
        "name": "Jabir",
        "email": "jabir@gmail.com",
        "password": "secret123"
    }

# Response Model with Status Code
@app.post(
    "/users",
    response_model=UserResponse,
    status_code=201
)
def create_user(user: UserCreate):
    return {
        "id": 1,
        "name": user.name,
        "email": user.email
    }

# Response Model Exclude
@app.get(
    "/user",
    response_model=UserResponse,
    response_model_exclude_none=True
)
def get_user():
    return {
        "id": 1,
        "name": "Jabir",
        "phone": None
    }

# Response Model Include
@app.get(
    "/user",
    response_model=UserResponse,
    response_model_include={"id", "name"}
)
def get_user():
    return {
        "id": 1,
        "name": "Jabir",
        "email": "jabir@gmail.com"
    }

# Response Model Exclude
@app.get(
    "/user",
    response_model=UserResponse,
    response_model_exclude={"email"}
)
def get_user():
    return {
        "id": 1,
        "name": "Jabir",
        "email": "jabir@gmail.com"
    }


# Created Status Code

from fastapi import status

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message": "User created"}

# Accepted

@app.post("/send-email")
def send_email():
    return {"message": "Email queued"}

# No Content

@app.delete("/users/{id}", status_code=204)
def delete_user(id: int):
    pass

# Not Found
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="User not found"
)


## FastAPI Example Using Multiple Status Codes

from fastapi import FastAPI, HTTPException, status

app = FastAPI()

users = {
    1: "John",
    2: "Alice"
}

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {
        "id": user_id,
        "name": users[user_id]
    }

@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED
)
def create_user():
    return {
        "message": "User created"
    }



# 
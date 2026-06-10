from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import ConfigDict


class UserCreate(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=100
    )

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=100
    )

    mobile: str = Field(
        min_length=10,
        max_length=15
    )


class UserLogin(BaseModel):

    email: EmailStr

    password: str


class UserResponse(BaseModel):

    id: int

    name: str

    email: EmailStr

    mobile: str

    model_config = ConfigDict(
        from_attributes=True
    )
from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from app.database.session import get_db

from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse
)

from app.schemas.token import Token

from app.services.user_service import UserService

from app.utils.jwt import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
async def register(
    payload: UserCreate,
    db: AsyncSession = Depends(get_db)
):

    return await UserService.register_user(
        db,
        payload
    )


@router.post(
    "/login",
    response_model=Token
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):

    user = await UserService.authenticate_user(
        db,
        form_data.username,  # email goes here
        form_data.password
    )

    if not user:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "user_id": user.id,
            "email": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
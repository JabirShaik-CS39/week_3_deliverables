from fastapi import HTTPException
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User

from app.schemas.user import UserCreate

from app.repositories.user_repository import UserRepository

from app.core.security import (
    hash_password,
    verify_password
)


class UserService:

    @staticmethod
    async def register_user(
        db: AsyncSession,
        payload: UserCreate
    ):

        existing_user = await UserRepository.get_by_email(
            db,
            payload.email
        )

        if existing_user:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        user = User(
            name=payload.name,
            email=payload.email,
            password=hash_password(
                payload.password
            ),
            mobile=payload.mobile
        )

        return await UserRepository.create(
            db,
            user
        )

    @staticmethod
    async def authenticate_user(
        db: AsyncSession,
        email: str,
        password: str
    ):

        user = await UserRepository.get_by_email(
            db,
            email
        )

        if not user:

            return None

        if not verify_password(
            password,
            user.password
        ):

            return None

        return user
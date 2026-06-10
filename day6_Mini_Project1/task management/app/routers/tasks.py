from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db

from app.core.dependencies import (
    get_current_user
)

from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
    TaskResponse
)

from app.services.task_service import (
    TaskService
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post(
    "",
    response_model=TaskResponse
)
async def create_task(
    payload: TaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await TaskService.create_task(
        db,
        payload,
        current_user.id
    )


@router.get(
    "",
    response_model=list[TaskResponse]
)
async def get_tasks(
    status: str | None = None,
    search: str | None = None,
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await TaskService.get_tasks(
        db,
        current_user.id,
        status,
        search,
        skip,
        limit
    )


@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
async def get_task(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await TaskService.get_task(
        db,
        task_id,
        current_user.id
    )


@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
async def update_task(
    task_id: int,
    payload: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await TaskService.update_task(
        db,
        task_id,
        payload,
        current_user.id
    )


@router.delete(
    "/{task_id}"
)
async def delete_task(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await TaskService.delete_task(
        db,
        task_id,
        current_user.id
    )
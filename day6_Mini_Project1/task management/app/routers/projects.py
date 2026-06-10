from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db

from app.core.dependencies import (
    get_current_user
)

from app.schemas.project import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse
)

from app.services.project_service import (
    ProjectService
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post(
    "",
    response_model=ProjectResponse
)
async def create_project(
    payload: ProjectCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await ProjectService.create_project(
        db,
        payload,
        current_user.id
    )


@router.get(
    "",
    response_model=list[ProjectResponse]
)
async def get_projects(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await ProjectService.get_projects(
        db,
        current_user.id
    )


@router.get(
    "/{project_id}",
    response_model=ProjectResponse
)
async def get_project(
    project_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await ProjectService.get_project(
        db,
        project_id,
        current_user.id
    )


@router.put(
    "/{project_id}",
    response_model=ProjectResponse
)
async def update_project(
    project_id: int,
    payload: ProjectUpdate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await ProjectService.update_project(
        db,
        project_id,
        payload,
        current_user.id
    )


@router.delete(
    "/{project_id}"
)
async def delete_project(
    project_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await ProjectService.delete_project(
        db,
        project_id,
        current_user.id
    )
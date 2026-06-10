from fastapi import HTTPException
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import Project

from app.schemas.project import (
    ProjectCreate,
    ProjectUpdate
)

from app.repositories.project_repository import (
    ProjectRepository
)


class ProjectService:

    @staticmethod
    async def create_project(
        db: AsyncSession,
        payload: ProjectCreate,
        user_id: int
    ):

        project = Project(
            name=payload.name,
            shift_mode=payload.shift_mode,
            user_id=user_id
        )

        return await ProjectRepository.create(
            db,
            project
        )

    @staticmethod
    async def get_projects(
        db: AsyncSession,
        user_id: int
    ):

        return await ProjectRepository.get_all_by_user(
            db,
            user_id
        )

    @staticmethod
    async def get_project(
        db: AsyncSession,
        project_id: int,
        user_id: int
    ):

        project = await ProjectRepository.get_by_id(
            db,
            project_id
        )

        if not project:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )

        if project.user_id != user_id:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied"
            )

        return project

    @staticmethod
    async def update_project(
        db: AsyncSession,
        project_id: int,
        payload: ProjectUpdate,
        user_id: int
    ):

        project = await ProjectService.get_project(
            db,
            project_id,
            user_id
        )

        update_data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():

            setattr(
                project,
                key,
                value
            )

        return await ProjectRepository.update(
            db,
            project
        )

    @staticmethod
    async def delete_project(
        db: AsyncSession,
        project_id: int,
        user_id: int
    ):

        project = await ProjectService.get_project(
            db,
            project_id,
            user_id
        )

        await ProjectRepository.delete(
            db,
            project
        )

        return {
            "message": "Project deleted successfully"
        }
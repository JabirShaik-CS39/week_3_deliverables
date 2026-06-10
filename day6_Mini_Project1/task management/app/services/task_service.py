from fastapi import HTTPException
from fastapi import status

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task import Task
from app.models.project import Project
from app.models.user import User

from app.schemas.task import (
    TaskCreate,
    TaskUpdate
)

from app.repositories.task_repository import (
    TaskRepository
)


class TaskService:

    @staticmethod
    async def create_task(
        db: AsyncSession,
        payload: TaskCreate,
        current_user_id: int
    ):

        project_result = await db.execute(
            select(Project).where(
                Project.id == payload.project_id
            )
        )

        project = project_result.scalar_one_or_none()

        if not project:

            raise HTTPException(
                status_code=404,
                detail="Project not found"
            )

        if project.user_id != current_user_id:

            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        user_result = await db.execute(
            select(User).where(
                User.id == payload.assigned_to
            )
        )

        assigned_user = user_result.scalar_one_or_none()

        if not assigned_user:

            raise HTTPException(
                status_code=404,
                detail="Assigned user not found"
            )

        task = Task(
            title=payload.title,
            description=payload.description,
            project_id=payload.project_id,
            assigned_to=payload.assigned_to
        )

        return await TaskRepository.create(
            db,
            task
        )

    @staticmethod
    async def get_task(
        db: AsyncSession,
        task_id: int,
        current_user_id: int
    ):

        task = await TaskRepository.get_by_id(
            db,
            task_id
        )

        if not task:

            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        project_result = await db.execute(
            select(Project).where(
                Project.id == task.project_id
            )
        )

        project = project_result.scalar_one()

        if project.user_id != current_user_id:

            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return task

    @staticmethod
    async def update_task(
        db: AsyncSession,
        task_id: int,
        payload: TaskUpdate,
        current_user_id: int
    ):

        task = await TaskService.get_task(
            db,
            task_id,
            current_user_id
        )

        update_data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():

            setattr(
                task,
                key,
                value
            )

        return await TaskRepository.update(
            db,
            task
        )

    @staticmethod
    async def delete_task(
        db: AsyncSession,
        task_id: int,
        current_user_id: int
    ):

        task = await TaskService.get_task(
            db,
            task_id,
            current_user_id
        )

        await TaskRepository.delete(
            db,
            task
        )

        return {
            "message": "Task deleted successfully"
        }

    @staticmethod
    async def get_tasks(
        db: AsyncSession,
        current_user_id: int,
        status_filter: str | None,
        search: str | None,
        skip: int,
        limit: int
    ):

        query = (
            select(Task)
            .join(Project)
            .where(
                Project.user_id == current_user_id
            )
        )

        if status_filter:

            query = query.where(
                Task.status == status_filter
            )

        if search:

            query = query.where(
                Task.title.ilike(
                    f"%{search}%"
                )
            )

        query = query.offset(skip).limit(limit)

        result = await db.execute(query)

        return result.scalars().all()
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import Project


class ProjectRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        project: Project
    ):
        db.add(project)

        await db.commit()

        await db.refresh(project)

        return project

    @staticmethod
    async def get_all_by_user(
        db: AsyncSession,
        user_id: int
    ):

        result = await db.execute(
            select(Project).where(
                Project.user_id == user_id
            )
        )

        return result.scalars().all()

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        project_id: int
    ):

        result = await db.execute(
            select(Project).where(
                Project.id == project_id
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def delete(
        db: AsyncSession,
        project: Project
    ):

        await db.delete(project)

        await db.commit()

    @staticmethod
    async def update(
        db: AsyncSession,
        project: Project
    ):

        await db.commit()

        await db.refresh(project)

        return project
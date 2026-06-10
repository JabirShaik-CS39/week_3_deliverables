from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    mobile: Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=False
    )

    projects = relationship(
        "Project",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    assigned_tasks = relationship(
        "Task",
        back_populates="assignee"
    )
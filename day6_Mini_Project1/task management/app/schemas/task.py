from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class TaskCreate(BaseModel):

    title: str = Field(
        min_length=2,
        max_length=255
    )

    description: str | None = None

    project_id: int

    assigned_to: int


class TaskUpdate(BaseModel):

    title: str | None = None

    description: str | None = None

    status: str | None = None

    assigned_to: int | None = None


class TaskResponse(BaseModel):

    id: int

    title: str

    description: str | None

    status: str

    project_id: int

    assigned_to: int

    model_config = ConfigDict(
        from_attributes=True
    )
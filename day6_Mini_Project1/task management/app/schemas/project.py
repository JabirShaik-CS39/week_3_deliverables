from pydantic import BaseModel
from pydantic import Field
from pydantic import ConfigDict


class ProjectCreate(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=150
    )

    shift_mode: str = Field(
        min_length=2,
        max_length=50
    )


class ProjectUpdate(BaseModel):

    name: str | None = None

    shift_mode: str | None = None


class ProjectResponse(BaseModel):

    id: int

    name: str

    user_id: int

    shift_mode: str

    model_config = ConfigDict(
        from_attributes=True
    )
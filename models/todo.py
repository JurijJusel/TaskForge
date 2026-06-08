from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class TodoCreate(BaseModel):
    project_id: UUID
    title: str
    description: Optional[str] = None


class TodoResponse(BaseModel):
    id: UUID
    project_id: UUID
    title: str
    description: Optional[str] = None
    is_done: bool = False

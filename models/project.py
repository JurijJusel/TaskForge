from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional
from models.users import User


class ProjectMember(BaseModel):
    user: User
    role: str  # "admin" arba "worker"


class Project(BaseModel):
    id: UUID
    name: str
    description: Optional[str] = None
    status: Optional[str] = None
    created_at: datetime
    members: list[ProjectMember] = []

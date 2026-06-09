from pydantic import BaseModel
from uuid import UUID


class Invitation(BaseModel):
    id: UUID
    project_id: UUID
    email: str
    role: str  # "admin" arba "worker"
    status: str  # "pending", "accepted", "declined"

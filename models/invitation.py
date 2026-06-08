from pydantic import BaseModel
from uuid import UUID


class InvitationCreate(BaseModel):
    project_id: UUID
    email: str
    role: str  # "admin" arba "worker"


class InvitationResponse(BaseModel):
    id: UUID
    project_id: UUID
    email: str
    role: str
    status: str  # "pending", "accepted", "declined"

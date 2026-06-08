from pydantic import BaseModel
from uuid import UUID


class UserProfile(BaseModel):
    name: str


class UserResponse(BaseModel):
    id: UUID
    email: str
    name: str | None = None

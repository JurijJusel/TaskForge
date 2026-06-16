from pydantic import BaseModel
from uuid import UUID



class UserAuth(BaseModel):
    email: str
    password: str


class UserAuthEmailReset(BaseModel):
    email: str


class UserProfile(BaseModel):
    name: str


class User(BaseModel):
    id: UUID
    email: str
    name: str | None = None

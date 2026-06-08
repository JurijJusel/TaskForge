from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class FileCreate(BaseModel):
    project_id: UUID
    name: str
    file_type: str  # "txt", "photo", "document"


class FileResponse(BaseModel):
    id: UUID
    project_id: UUID
    name: str
    file_type: str
    file_url: str
    created_at: datetime

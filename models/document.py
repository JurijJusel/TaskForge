from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class Document(BaseModel):
    id: UUID
    project_id: UUID
    name: str
    file_type: str  # "txt", "photo", "document"
    file_url: str
    created_at: datetime
    updated_at: datetime


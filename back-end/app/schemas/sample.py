from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class SampleBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = True

class SampleCreate(SampleBase):
    title: str

class SampleUpdate(SampleBase):
    pass

class Sample(SampleBase):
    id: int
    created_at: datetime
    updated_at: datetime
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    deleted_at: Optional[datetime] = None
    deleted_by: Optional[int] = None
    is_deleted: bool = False
    status: bool = True

    class Config:
        from_attributes = True

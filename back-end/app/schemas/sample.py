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

    class Config:
        from_attributes = True

from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base, AuditModel

class Sample(Base, AuditModel):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    is_active = Column(Boolean, default=True)

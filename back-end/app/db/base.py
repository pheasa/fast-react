from typing import Any
from datetime import datetime
from sqlalchemy import Column, DateTime, BigInteger, Boolean, ForeignKey
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import relationship

from app.models.user import User

@as_declarative()
class Base:
    id: Any
    __name__: str
    
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

class AuditModel:
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    created_by = Column(BigInteger, ForeignKey(User.id), nullable=True)
    creator = relationship(User, foreign_keys=[created_by])
    updated_by = Column(BigInteger, ForeignKey(User.id), nullable=True)
    updater = relationship(User, foreign_keys=[updated_by])
    deleted_by = Column(BigInteger, ForeignKey(User.id), nullable=True)
    deleter = relationship(User, foreign_keys=[deleted_by])
    is_deleted = Column(Boolean, default=False, nullable=False)
    status = Column(Boolean, default=True, nullable=False)
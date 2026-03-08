from sqlalchemy import Column, DateTime, BigInteger, Boolean, ForeignKey, func
from sqlalchemy.orm import declared_attr, relationship
from app.models.user import User

class AuditModel:
    created_at = Column(DateTime, default=func.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=func.utcnow(), onupdate=func.utcnow(), nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    created_by = Column(BigInteger, ForeignKey(User.id), nullable=True)
    updated_by = Column(BigInteger, ForeignKey(User.id), nullable=True)
    deleted_by = Column(BigInteger, ForeignKey(User.id), nullable=True)
    is_deleted = Column(Boolean, default=False, nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    @declared_attr
    def creator(cls):
        return relationship(User, foreign_keys=[cls.created_by])
    
    @declared_attr
    def updater(cls):
        return relationship(User, foreign_keys=[cls.updated_by])
    
    @declared_attr
    def deleter(cls):
        return relationship(User, foreign_keys=[cls.deleted_by])
    
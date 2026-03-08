from datetime import datetime
from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    
    # Audit fields for User model itself
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    is_deleted = Column(Boolean, default=False, nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    created_by = Column(BigInteger, ForeignKey("user.id"), nullable=True)
    updated_by = Column(BigInteger, ForeignKey("user.id"), nullable=True)
    deleted_by = Column(BigInteger, ForeignKey("user.id"), nullable=True)

    # Self Relationships
    creator = relationship("User", remote_side=[id], foreign_keys=[created_by])
    updater = relationship("User", remote_side=[id], foreign_keys=[updated_by])
    deleter = relationship("User", remote_side=[id], foreign_keys=[deleted_by])

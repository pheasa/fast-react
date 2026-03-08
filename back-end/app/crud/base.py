from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.base import Base
from app.models.user import User

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], user: User, db: Session):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model
        self.user = user
        self.db = db

    def get(self, id: int) -> Optional[ModelType]:
        """
        Use .first() after call this function to get the result.
        """
        return self.db.query(self.model).filter(self.model.id == id, self.model.is_deleted.is_(False))
    
    def get_by_creator(self, id: int) -> Optional[ModelType]:
        """
        Use .first() after call this function to get the result.
        """
        return self.db.query(self.model).filter(self.model.id == id, self.model.is_deleted.is_(False), self.model.created_by == self.user.id)
    
    def get_multi(
        self, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        """
        Use .all() after call this function to get the result.
        """
        return self.db.query(self.model).filter(self.model.is_deleted.is_(False)).offset(skip).limit(limit)
    
    def get_multi_by_creator(
        self, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        """
        Use .all() after call this function to get the result.
        """
        return self.db.query(self.model).filter(self.model.is_deleted.is_(False), self.model.created_by == self.user.id).offset(skip).limit(limit)

    def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = obj_in.model_dump()
        db_obj = self.model(**obj_in_data)
        db_obj.creator = self.user
        self.db.add(db_obj)
        self.db.refresh(db_obj)
        return db_obj

    def update(
        self,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        for field in update_data:
            if hasattr(db_obj, field):
                setattr(db_obj, field, update_data[field])
        self.db_obj.updater = self.user
        self.db.add(db_obj)
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, *, id: int) -> ModelType:
        obj = self.db.query(self.model).get(id)
        obj.is_deleted = True
        obj.deleter = self.user
        return obj
    
    def commit(self):
        self.db.commit()

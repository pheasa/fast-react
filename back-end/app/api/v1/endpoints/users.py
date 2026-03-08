from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Any
from app.schemas.user import User, UserCreate
from app.schemas.response import BaseResponse, PaginatedResponse
from app.services.pagination import paginate
from app.api import deps
from app.crud import crud_user

router = APIRouter()

@router.get("/", response_model=BaseResponse[List[User]])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    users = crud_user.user.get_multi(db, skip=skip, limit=limit)
    return BaseResponse(data=users)

@router.post("/", response_model=BaseResponse[User])
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate
) -> Any:
    user = crud_user.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud_user.user.create(db, obj_in=user_in)
    return BaseResponse(data=user)

@router.get("/list", response_model=PaginatedResponse[User])
def list_users(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    db: Session = Depends(deps.get_db)
):
    all_users = crud_user.user.get_multi(db, skip=0, limit=1000)
    paginated_data = paginate(all_users, page, limit)
    return PaginatedResponse(data=paginated_data)

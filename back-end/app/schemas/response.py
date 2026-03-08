from typing import Generic, TypeVar, Optional, Any, List
from pydantic import BaseModel

T = TypeVar("T")

class BaseResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str = "Success"
    data: Optional[T] = None
    error: Optional[Any] = None

class PaginatedData(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    limit: int
    total_pages: int

class PaginatedResponse(BaseResponse[PaginatedData[T]], Generic[T]):
    pass

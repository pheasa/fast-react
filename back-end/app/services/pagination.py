import math
from typing import List, TypeVar
from app.schemas.response import PaginatedData

T = TypeVar("T")

def paginate(items: List[T], page: int, limit: int) -> PaginatedData[T]:
    total = len(items)
    total_pages = math.ceil(total / limit) if limit > 0 else 0
    
    start = (page - 1) * limit
    end = start + limit
    paginated_items = items[start:end]
    
    return PaginatedData(
        items=paginated_items,
        total=total,
        page=page,
        limit=limit,
        total_pages=total_pages
    )

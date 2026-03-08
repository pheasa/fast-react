from fastapi import APIRouter, Query
from typing import List
from app.schemas.sample import Sample
from app.schemas.response import BaseResponse, PaginatedResponse
from app.services.pagination import paginate

router = APIRouter()

@router.get("/", response_model=BaseResponse[List[Sample]])
def read_samples():
    samples = [{"id": 1, "title": "Sample 1"}, {"id": 2, "title": "Sample 2"}]
    return BaseResponse(data=samples)

@router.get("/list", response_model=PaginatedResponse[Sample])
def list_samples(
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Samples per page")
):
    # Dummy data for demonstration
    all_samples = [{"id": i, "title": f"Sample {i}"} for i in range(1, 51)]
    
    # Use the reusable pagination logic
    paginated_data = paginate(all_samples, page, limit)
    
    return PaginatedResponse(data=paginated_data)

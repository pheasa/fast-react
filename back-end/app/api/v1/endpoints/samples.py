from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Any
from datetime import datetime
from app.schemas.sample import Sample, SampleCreate, SampleUpdate
from app.schemas.response import BaseResponse, PaginatedResponse
from app.services.pagination import paginate
from app.api import deps
from app.crud import crud_sample

router = APIRouter()

@router.get("/", response_model=BaseResponse[List[Sample]])
def read_samples(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve samples.
    """
    samples = crud_sample.sample.get_multi(db, skip=skip, limit=limit)
    return BaseResponse(data=samples)

@router.post("/", response_model=BaseResponse[Sample])
def create_sample(
    *,
    db: Session = Depends(deps.get_db),
    sample_in: SampleCreate
) -> Any:
    """
    Create new sample.
    """
    sample = crud_sample.sample.create(db, obj_in=sample_in)
    return BaseResponse(data=sample)

@router.put("/{id}", response_model=BaseResponse[Sample])
def update_sample(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    sample_in: SampleUpdate
) -> Any:
    """
    Update a sample.
    """
    sample = crud_sample.sample.get(db, id=id)
    if not sample:
        raise HTTPException(status_code=404, detail="Sample not found")
    sample = crud_sample.sample.update(db, db_obj=sample, obj_in=sample_in)
    return BaseResponse(data=sample)

@router.get("/list", response_model=PaginatedResponse[Sample])
def list_samples(
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Samples per page"),
    db: Session = Depends(deps.get_db)
):
    """
    Retrieve samples with pagination.
    """
    # For now, we still use the paginate utility which expects a list.
    # In a real app, you might want a paginate_db utility that uses SQL offset/limit.
    all_samples = crud_sample.sample.get_multi(db, skip=0, limit=1000) # Simple fetch for demo
    
    # If no data in DB, use dummy data for demonstration
    if not all_samples:
        now = datetime.utcnow()
        all_samples = [{
            "id": i, 
            "title": f"Sample {i}", 
            "description": f"Desc {i}", 
            "is_active": True,
            "created_at": now,
            "updated_at": now,
            "created_by": 1,
            "updated_by": 1,
            "deleted_at": None,
            "deleted_by": None,
            "is_deleted": False,
            "status": True
        } for i in range(1, 51)]
    
    paginated_data = paginate(all_samples, page, limit)
    
    return PaginatedResponse(data=paginated_data)

@router.get("/{id}", response_model=BaseResponse[Sample])
def read_sample(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Get sample by ID.
    """
    sample = crud_sample.sample.get(db, id=id)
    if not sample:
        raise HTTPException(status_code=404, detail="Sample not found")
    return BaseResponse(data=sample)

@router.delete("/{id}", response_model=BaseResponse[Sample])
def delete_sample(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Delete a sample.
    """
    sample = crud_sample.sample.get(db, id=id)
    if not sample:
        raise HTTPException(status_code=404, detail="Sample not found")
    sample = crud_sample.sample.remove(db, id=id)
    return BaseResponse(data=sample)

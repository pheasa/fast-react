from fastapi import APIRouter
from typing import List
from app.schemas.item import Item
from app.schemas.response import BaseResponse

router = APIRouter()

@router.get("/", response_model=BaseResponse[List[Item]])
def read_items():
    items = [{"id": 1, "title": "Foo"}, {"id": 2, "title": "Bar"}]
    return BaseResponse(data=items)

from fastapi import APIRouter
from app.api.v1.endpoints import samples, users

api_router = APIRouter()
api_router.include_router(samples.router, prefix="/samples", tags=["samples"])
api_router.include_router(users.router, prefix="/users", tags=["users"])

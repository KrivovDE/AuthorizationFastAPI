from fastapi import APIRouter
from .endpoints import users_router

api_router = APIRouter(prefix="/v1")

api_router.include_router(users_router)

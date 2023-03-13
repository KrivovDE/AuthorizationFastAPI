from fastapi import APIRouter
from .v1 import api_router as v1_api_router

api_router = APIRouter(prefix="/api")

api_router.include_router(v1_api_router)

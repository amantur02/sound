from api.api_v1 import auth_endpoints as auth_router
from api.api_v1 import mp3_endpoints as mp3_router
from api.api_v1 import customer_endpoints as customer_router
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(
    auth_router.router, prefix="/auth", tags=["authentication"]
)
api_router.include_router(mp3_router.router, prefix="/mp3", tags=["mp3"])
api_router.include_router(
    customer_router.router, prefix="/customers", tags=["customers"]
)

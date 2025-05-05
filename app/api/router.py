from fastapi import APIRouter

from app.api.users.routes import users_api_router

api_router = APIRouter(tags=["api"])

api_router.include_router(users_api_router, prefix="/users")

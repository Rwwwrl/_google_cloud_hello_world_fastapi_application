from fastapi import APIRouter

from app.api.hello_world.routes import hello_world_api_router
from app.api.users.routes import users_api_router
from app.api.wearables.routes import wearables_router

api_router = APIRouter(tags=["api"])

api_router.include_router(users_api_router, prefix="/users")
api_router.include_router(hello_world_api_router, prefix="/hello-world")
api_router.include_router(wearables_router, prefix="/wearables")

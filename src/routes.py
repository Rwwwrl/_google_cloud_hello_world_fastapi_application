from fastapi import APIRouter

from src.models import User
from src.settings import settings

api_router = APIRouter(prefix="/api")


@api_router.get("/")
def hello_world():
    return {"message": "Hello, World!"}


@api_router.get("/get_env_variable")
def get_env_variable():
    return {"env variable": settings.MY_SECRET_VALUE}


@api_router.get("/get_users")
async def get_users() -> list[int]:
    return [user.id for user in await User.find().to_list()]

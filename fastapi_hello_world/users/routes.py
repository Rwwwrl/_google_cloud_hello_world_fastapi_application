from fastapi import APIRouter

from fastapi_hello_world.users.models import User

users_api_router = APIRouter(tags=["users"])


@users_api_router.get("/get_users")
async def get_users() -> list[int]:
    return [user.id for user in await User.find().to_list()]

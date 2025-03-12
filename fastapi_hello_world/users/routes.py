from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from fastapi_hello_world.core.settings import BASE_DIR, settings
from fastapi_hello_world.users.models import User

users_api_router = APIRouter(tags=["users"])

templates = Jinja2Templates(directory=BASE_DIR / "users" / "templates")


@users_api_router.get("")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "api_key": settings.FIREBASE_CONFIG.api_key,
            "auth_domain": settings.FIREBASE_CONFIG.auth_domain,
        },
    )


@users_api_router.get("/get_users")
async def get_users() -> list[int]:
    return [user.id for user in await User.find().to_list()]

from fastapi import APIRouter

from fastapi_hello_world.core.settings import settings

tmp_app_api_router = APIRouter(tags=["tmp-app"])


@tmp_app_api_router.get("/")
def hello_world():
    return {"message": "Hello, World!"}


@tmp_app_api_router.get("/get_env_variable")
def get_env_variable():
    return {"env variable": settings.MY_SECRET_VALUE}

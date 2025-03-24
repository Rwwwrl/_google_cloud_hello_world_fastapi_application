from fastapi import APIRouter, FastAPI, Response, status
from fastapi.staticfiles import StaticFiles

from fastapi_hello_world.core.lifespan import lifespan
from fastapi_hello_world.users.routes import users_api_router

app = FastAPI(lifespan=lifespan)


api_router = APIRouter(prefix="/api")
api_router.include_router(users_api_router, prefix="/users")


@app.get("/liveness_check")
def liveness_check():
    return Response(status_code=status.HTTP_200_OK)


@app.get("/readiness_check")
def readiness_check():
    return Response(status_code=status.HTTP_200_OK)


app.include_router(router=api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

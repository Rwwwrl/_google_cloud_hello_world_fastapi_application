from fastapi import FastAPI, Request, Response, status
from fastapi.staticfiles import StaticFiles

from app.api.router import api_router
from app.core.lifespan import lifespan
from app.core.mongodb.health_check import HealthCheckFailed as MongoDBHealthCheckFailed
from app.core.mongodb.health_check import mongodb_health_check

app = FastAPI(lifespan=lifespan)


@app.get(
    "/liveness_check",
    responses={
        status.HTTP_200_OK: {},
    },
)
def liveness_check():
    return Response(status_code=status.HTTP_200_OK)


@app.get(
    "/readiness_check",
    responses={
        status.HTTP_200_OK: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def readiness_check(request: Request):
    mongodb_database = request.app.state.mongodb_database
    try:
        await mongodb_health_check(db=mongodb_database)
    except MongoDBHealthCheckFailed:
        return Response(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    return Response(status_code=status.HTTP_200_OK)


app.include_router(router=api_router, prefix="/api")

app.mount("/static", StaticFiles(directory="static"), name="static")

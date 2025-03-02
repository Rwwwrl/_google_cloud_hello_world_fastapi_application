from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI, Response, status
from motor.motor_asyncio import AsyncIOMotorClient

from src.routes import api_router
from src.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
    await init_beanie(
        database=client["my_db"],
        document_models=[
            "src.models.User",
        ],
    )
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/liveness_check")
def liveness_check():
    return Response(status_code=status.HTTP_200_OK)


@app.get("/readiness_check")
def readiness_check():
    return Response(status_code=status.HTTP_200_OK)


app.include_router(router=api_router)

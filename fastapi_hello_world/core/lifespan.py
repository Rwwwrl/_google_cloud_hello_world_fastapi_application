from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from fastapi_hello_world.core.settings import settings


async def on_startup_event(app: FastAPI) -> None:
    client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
    await init_beanie(
        database=client["fastapi_hello_world"],
        document_models=[
            "fastapi_hello_world.users.models.User",
        ],
    )


async def on_shutdown_event(app: FastAPI) -> None:
    pass


@asynccontextmanager
async def lifespan(app: FastAPI):
    await on_startup_event(app=app)
    yield
    await on_shutdown_event(app=app)

from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.settings import settings


async def on_startup_event(app: FastAPI) -> None:
    client = AsyncIOMotorClient(settings.MONGO_DB_CONFIG.uri)
    database = client[settings.MONGO_DB_CONFIG.db_name]
    await init_beanie(
        database=database,
        document_models=[
            "app.api.users.documents.User",
        ],
    )

    app.state.mongodb_database = database


async def on_shutdown_event(app: FastAPI) -> None:
    pass


@asynccontextmanager
async def lifespan(app: FastAPI):
    await on_startup_event(app=app)
    yield
    await on_shutdown_event(app=app)

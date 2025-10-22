from contextlib import asynccontextmanager
from typing import cast

from fastapi import FastAPI
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from vital import AsyncVital

from app.core.mongodb.get_mongodb_client import get_mongodb_client
from app.core.settings import settings


async def on_startup_event(app: FastAPI) -> None:
    mongodb_client = get_mongodb_client()
    await mongodb_client.initiate_beanie(skip_indexes=False)

    app.state.mongodb_client = mongodb_client

    app.state.httpx_async_client = AsyncClient()

    app.state.async_vital = AsyncVital(
        api_key=settings.WEARABLES_JUNCTION_CONFIG.team_api_key,
        environment=settings.WEARABLES_JUNCTION_CONFIG.environment,
        httpx_client=app.state.httpx_async_client,
    )


async def on_shutdown_event(app: FastAPI) -> None:
    cast(AsyncIOMotorClient, app.state.mongodb_client).close()
    await cast(AsyncClient, app.state.httpx_async_client).aclose()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await on_startup_event(app=app)
    yield
    await on_shutdown_event(app=app)

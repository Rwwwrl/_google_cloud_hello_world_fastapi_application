import asyncio

import pytest_asyncio
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.api.app import app
from app.api.users.documents import User
from app.core.settings import settings


@pytest_asyncio.fixture(scope="session")
async def mongodb_client():
    """
    Set up a test database for the session.
    """
    test_db_uri = settings.MONGO_DB_CONFIG.uri
    client = AsyncIOMotorClient(test_db_uri)
    client.get_io_loop = asyncio.get_event_loop
    database_name = "test"
    db = client.get_database(database_name)

    await init_beanie(
        database=db,
        document_models=[
            User,
        ],
    )

    app.state.mongo_client = client

    yield client

    await client.drop_database(database_name)


@pytest_asyncio.fixture(scope="function", autouse=True)
async def clear_collections(mongodb_client):
    """
    Clear all collections before each test.
    """
    for model in [User]:
        await model.get_motor_collection().delete_many({})
    yield

from datetime import timezone

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient


class MongoDBClient:
    def __init__(self, uri: str, database_name: str):
        self.async_motor_client = AsyncIOMotorClient(
            uri,
            tz_aware=True,
            tzinfo=timezone.utc,
            socketTimeoutMS=60000,
            connectTimeoutMS=60000,
        )
        self._db = self.async_motor_client[database_name]

    async def initiate_beanie(self, skip_indexes: bool = True) -> None:
        await init_beanie(
            database=self._db,
            skip_indexes=skip_indexes,
            document_models=[
                "app.api.users.models.User",
            ],
        )

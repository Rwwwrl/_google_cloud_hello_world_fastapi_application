from app.core.mongodb.mongodb_client import MongoDBClient
from app.core.settings import settings

__all__ = ("get_mongodb_client",)


def get_mongodb_client() -> MongoDBClient:
    return MongoDBClient(
        uri=settings.MONGO_DB_CONFIG.uri,
        database_name=settings.MONGO_DB_CONFIG.db_name,
    )

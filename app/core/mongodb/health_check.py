from uuid import uuid4

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase


class HealthCheckFailed(Exception):
    pass


async def mongodb_health_check(db: AsyncIOMotorDatabase) -> None:
    collection_for_health_check = "__mongodb_health_check__"

    async def _read_operation() -> None:
        entry = await db[collection_for_health_check].find_one(
            {"_id": ObjectId("111111111111111111111111")},
        )

        assert entry is not None

    async def _write_operation() -> None:
        update_result = await db[collection_for_health_check].update_one(
            {"_id": ObjectId("111111111111111111111111")},
            {"$set": {"value": str(uuid4())}},
        )
        assert update_result.modified_count == 1

    try:
        await _read_operation()
    except Exception:
        raise HealthCheckFailed("read operation have not passed health check")

    try:
        await _write_operation()
    except Exception:
        raise HealthCheckFailed("write operation have not passed health check")

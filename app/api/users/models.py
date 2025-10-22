from beanie import Document
from pymongo import ASCENDING, IndexModel

from app.api.users.schemas import nested_models


class User(Document):
    class Settings:
        name = "users"
        indexes = [
            IndexModel(
                [("google_identity.uid", ASCENDING)],
                name="uid__unique",
                unique=True,
            ),
            IndexModel(
                [("id_in_vital", ASCENDING)],
                name="id_in_vital__unique",
                unique=True,
                partialFilterExpression={"id_in_vital": {"$exists": True, "$type": "string"}},
            ),
        ]

    google_identity: nested_models.GCloudIdentityPlatformDataDTO
    id_in_vital: str | None

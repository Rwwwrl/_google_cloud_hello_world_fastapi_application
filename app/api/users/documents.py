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
        ]

    google_identity: nested_models.GCloudIdentityPlatformDataDTO

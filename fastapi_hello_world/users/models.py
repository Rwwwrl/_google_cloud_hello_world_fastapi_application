from beanie import Document
from pymongo import ASCENDING, IndexModel

from fastapi_hello_world.core.common.dto import DTO


class GoogleIdentityPlatformData(DTO):
    uid: str
    email: str


class User(Document):
    google_identity: GoogleIdentityPlatformData

    class Settings:
        name = "users"
        indexes = [
            IndexModel(
                [("google_identity.uid", ASCENDING)],
                name="uid__unique",
                unique=True,
            ),
        ]

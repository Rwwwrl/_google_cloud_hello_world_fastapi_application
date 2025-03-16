from beanie import Document
from pymongo import ASCENDING, IndexModel

from fastapi_hello_world.core.common.dto import DTO


class GoogleIdentityPlatformData(DTO):
    uid: str
    tenant_id: str
    email: str | None


class User(Document):
    google_identity: GoogleIdentityPlatformData

    class Settings:
        name = "users"
        indexes = [
            IndexModel(
                [
                    ("google_identity.tenant_id", ASCENDING),
                    ("google_identity.uid", ASCENDING),
                ],
                name="tenant_id__uid__unique",
                unique=True,
            ),
        ]

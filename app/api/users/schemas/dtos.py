from beanie import PydanticObjectId
from pydantic import EmailStr

from app.core.common.dto import DTO


class GCloudIdentityPlatformDataDTO(DTO):
    uid: str
    email: EmailStr


class CreateNewUserDTO(DTO):
    google_identity: GCloudIdentityPlatformDataDTO


class BaseUserDTO(DTO):
    id: PydanticObjectId
    google_identity: GCloudIdentityPlatformDataDTO
    id_in_vital: str | None

    @classmethod
    def from_motor_doc(cls, doc: dict) -> "BaseUserDTO":
        _id = doc.pop("_id")
        return BaseUserDTO(
            id=_id,
            **doc,
        )

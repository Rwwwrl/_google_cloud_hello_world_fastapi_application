from pydantic import EmailStr

from app.core.common.dto import DTO


class GCloudIdentityPlatformDataDTO(DTO):
    uid: str
    email: EmailStr


class CreateNewUserDTO(DTO):
    google_identity: GCloudIdentityPlatformDataDTO


class UserDTO(DTO):
    google_identity: GCloudIdentityPlatformDataDTO

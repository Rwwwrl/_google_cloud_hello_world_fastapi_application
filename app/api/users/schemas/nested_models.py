from pydantic import EmailStr

from app.core.base_schemas import BaseNestedModel


class GCloudIdentityPlatformDataDTO(BaseNestedModel):
    uid: str
    email: EmailStr

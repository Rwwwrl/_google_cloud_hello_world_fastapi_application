from motor.motor_asyncio import AsyncIOMotorClientSession

from fastapi_hello_world.core.common.dto import DTO
from fastapi_hello_world.users import models


class GoogleIdentityPlatformDataDTO(DTO):
    uid: str
    tenant_id: str
    email: str | None


class CreateNewUserDTO(DTO):
    google_identity: GoogleIdentityPlatformDataDTO


class ExceptionDuringWriting(Exception):
    def __init__(self, original_exception: Exception):
        super().__init__(original_exception)
        self.original_exception = original_exception


class UserRepository:
    @classmethod
    async def create_new_user(
        cls,
        new_user_payload: CreateNewUserDTO,
        session: AsyncIOMotorClientSession,
    ) -> models.User:
        new_user = models.User(
            google_identity=models.GoogleIdentityPlatformData(
                uid=new_user_payload.google_identity.uid,
                tenant_id=new_user_payload.google_identity.tenant_id,
                email=new_user_payload.google_identity.email,
            )
        )
        try:
            return await new_user.insert(session=session)
        except Exception as e:
            raise ExceptionDuringWriting(original_exception=e)

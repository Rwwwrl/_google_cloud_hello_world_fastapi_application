from motor.motor_asyncio import AsyncIOMotorClientSession

from app.api.users.documents import User
from app.api.users.schemas import dtos, nested_models
from app.api.users.schemas.dtos import UserDTO


class UserRepository:
    @classmethod
    async def create_new_user(
        cls,
        create_new_user_payload: dtos.CreateNewUserDTO,
        session: AsyncIOMotorClientSession | None = None,
    ) -> User:
        new_user = User(
            google_identity=nested_models.GCloudIdentityPlatformDataDTO(
                uid=create_new_user_payload.google_identity.uid,
                email=create_new_user_payload.google_identity.email,
            )
        )
        new_user = await new_user.insert(session=session)
        return UserDTO(**new_user)

from beanie import PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClientSession

from app.api.users.models import User
from app.api.users.schemas import dtos, nested_models


class UserRepository:
    @classmethod
    async def create_new_user(
        cls,
        create_new_user_payload: dtos.CreateNewUserDTO,
        session: AsyncIOMotorClientSession | None = None,
    ) -> dtos.BaseUserDTO:
        new_user = User(
            google_identity=nested_models.GCloudIdentityPlatformDataDTO(
                uid=create_new_user_payload.google_identity.uid,
                email=create_new_user_payload.google_identity.email,
            ),
            id_in_vital=None,
        )
        new_user = await new_user.insert(session=session)
        return dtos.BaseUserDTO(**new_user.model_dump())

    @classmethod
    async def find_by_id(
        cls,
        _id: PydanticObjectId,
    ) -> dtos.BaseUserDTO:
        doc = await User.get_motor_collection().find_one({"_id": _id})

        return dtos.BaseUserDTO.from_motor_doc(doc)

    @classmethod
    async def update_by_id(
        cls,
        _id: PydanticObjectId,
        update_data: dict,
    ) -> None:
        _ = await User.get_motor_collection().update_one(
            {
                "_id": _id,
            },
            {"$set": update_data},
        )

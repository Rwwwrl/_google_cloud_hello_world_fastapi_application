from fastapi import APIRouter, HTTPException, status

from app.api.users.exceptions import UserNotFound
from app.api.users.repositories import UserRepository
from app.api.wearables.dependecies import AsyncVital
from app.api.wearables.schemas import request_schemas, response_schemas

wearables_router = APIRouter(tags=["wearables"])


@wearables_router.post(
    "/generate-link-token",
    status_code=status.HTTP_200_OK,
)
async def generate_link_token(
    payload: request_schemas.GenerateLinkTokenRequestPayload,
    async_vital: AsyncVital,
) -> response_schemas.GeneratedLinkTokenSchema:
    try:
        user = await UserRepository.find_by_id(_id=payload.user_id)
    except UserNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")

    if user.id_in_vital is None:
        _user_client_facing_key = await async_vital.user.create(client_user_id=str(user.id))

        user_id_in_vital = _user_client_facing_key.user_id

        await UserRepository.update_by_id(_id=user.id, update_data={"id_in_vital": user_id_in_vital})
    else:
        user_id_in_vital = user.id_in_vital

    token = await async_vital.link.token(user_id=user_id_in_vital)

    return response_schemas.GeneratedLinkTokenSchema(
        link_token=token.link_token,
    )

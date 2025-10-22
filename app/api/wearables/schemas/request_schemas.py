from beanie import PydanticObjectId

from app.core.base_schemas import BaseRequestSchema


class GenerateLinkTokenRequestPayload(BaseRequestSchema):
    user_id: PydanticObjectId

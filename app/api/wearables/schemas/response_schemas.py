from app.core.base_schemas import BaseResponseSchema


class GeneratedLinkTokenSchema(BaseResponseSchema):
    link_token: str

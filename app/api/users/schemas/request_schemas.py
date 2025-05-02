from pydantic import EmailStr

from app.core.base_schemas import BaseRequestSchema


class CreateUserPayload(BaseRequestSchema):
    uid: str
    email: EmailStr

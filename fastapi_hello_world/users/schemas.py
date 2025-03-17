from pydantic import EmailStr

from fastapi_hello_world.core.base_schemas.base_fastapi_schema import BaseFastApiSchema


class CreateUserPayload(BaseFastApiSchema):
    uid: str
    email: EmailStr

from pydantic import EmailStr, Field

from fastapi_hello_world.core.base_schemas.base_fastapi_schema import BaseFastApiSchema


class CreateUserPayload(BaseFastApiSchema):
    uid: str
    tenant_id: str | None = Field(description="note: In single-tenancy tenant_id is always None")
    email: EmailStr

from pydantic import BaseModel, ConfigDict

__all__ = ("DTO",)


class DTO(BaseModel, frozen=True):
    model_config = ConfigDict(extra="forbid")

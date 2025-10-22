from pathlib import Path

from pydantic import BaseModel, field_validator
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)
from vital.environment import VitalEnvironment

BASE_DIR = Path(__file__).resolve().parent.parent


class FirebaseConfig(BaseModel):
    api_key: str
    auth_domain: str


class MongoDBConfig(BaseModel):
    uri: str
    db_name: str


class WearablesJunctionConfig(BaseModel):
    team_api_key: str
    environment: VitalEnvironment

    @field_validator("environment", mode="before")
    @classmethod
    def parse_environment(cls, value: str | VitalEnvironment) -> VitalEnvironment:
        match value:
            case str():
                if value.upper() in VitalEnvironment.__members__:
                    return VitalEnvironment[value.upper()]

                return VitalEnvironment(value)

            case VitalEnvironment():
                return value


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        yaml_file="env.yaml",
        env_ignore_empty=False,
        extra="ignore",
    )

    MONGO_DB_CONFIG: MongoDBConfig

    AUDIENCE: str

    FIREBASE_CONFIG: FirebaseConfig

    WEARABLES_JUNCTION_CONFIG: WearablesJunctionConfig

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            YamlConfigSettingsSource(settings_cls),
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
        )


settings = Settings()  # type: ignore

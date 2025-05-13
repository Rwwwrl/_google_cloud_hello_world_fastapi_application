from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)

BASE_DIR = Path(__file__).resolve().parent.parent


class FirebaseConfig(BaseModel):
    api_key: str
    auth_domain: str


class MongoDBConfig(BaseModel):
    uri: str
    db_name: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        yaml_file="env.yaml",
        env_ignore_empty=False,
        extra="ignore",
    )

    MONGO_DB_CONFIG: MongoDBConfig

    AUDIENCE: str

    FIREBASE_CONFIG: FirebaseConfig

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

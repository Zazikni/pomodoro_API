from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn


class SettingsApplicationRun(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8080


class SettingsDatabase(BaseModel):
    URL: PostgresDsn
    ECHO: bool = True
    MAX_OVERFLOW: int = 10
    POOL_SIZE: int = 10
    NAMING_CONVENTIONS: dict = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(
            ".env.template",
            ".env",
        ),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="POMODORO__",
    )
    run: SettingsApplicationRun = SettingsApplicationRun()
    database: SettingsDatabase


settings = Settings()

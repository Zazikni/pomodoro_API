from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class SettingsApplicationRun(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8080


class SettingsDatabase(BaseModel):
    URL: str
    ECHO: bool = True
    MAX_OVERFLOW: int = 10
    POOL_SIZE: int = 10


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

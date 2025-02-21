from pydantic_settings import BaseSettings
from pydantic import BaseModel


class SettingsApplicationRun(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8080


class SettingsDatabase(BaseModel):
    DATABASE_URL: str = "sqlite+aiosqlite:///./pomodoro_database.sqlite3"
    SQLALCHEMY_ECHO: bool = True
    MAX_OVERFLOW: int = 10
    POOL_SIZE: int = 10


class Settings(BaseSettings):
    run: SettingsApplicationRun = SettingsApplicationRun()
    database: SettingsDatabase = SettingsDatabase()


settings = Settings()

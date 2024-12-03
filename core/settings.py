from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./pomodoro_database.sqlite3"
    SQLALCHEMY_ECHO: bool = True


settings = Settings()

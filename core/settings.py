from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = "sqlite+aiosqlite:///./pomodoro_database.sqlite3"


settings = Settings()

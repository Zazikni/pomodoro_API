from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GOOGLE_TOKEN: str = "1234"
    DB_URL: str = "sqlite://pomodoro_database.db"

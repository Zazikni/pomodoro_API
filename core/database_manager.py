from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .settings import settings


class DatabaseManager:
    def __init__(self):
        self.engine = create_async_engine(
            url=settings.DATABASE_URL,
            echo=settings.SQLALCHEMY_ECHO,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


database_manager = DatabaseManager()

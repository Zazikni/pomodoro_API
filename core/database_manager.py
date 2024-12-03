from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)
from asyncio import current_task

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

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self.get_scoped_session() as session:
            yield session
            await session.remove()


database_manager = DatabaseManager()

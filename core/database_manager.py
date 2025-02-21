from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
    AsyncEngine,
)
from asyncio import current_task

from .settings import settings


class DatabaseManager:
    def __init__(
        self,
        url: str,
        echo: bool,
        # max_overflow: int,
        # pool_size: int,
    ):
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            # max_overflow=max_overflow,
            # pool_size=pool_size,
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
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        yield session
        await session.remove()

    async def dispose(self):
        await self.engine.dispose()


database_manager = DatabaseManager(
    url=settings.database.DATABASE_URL,
    echo=settings.database.SQLALCHEMY_ECHO,
    # max_overflow=settings.database.MAX_OVERFLOW,
    # pool_size=settings.database.POOL_SIZE,
)

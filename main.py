from contextlib import asynccontextmanager

from fastapi import FastAPI
from tasks.views import router as task_router
from core.models import Base
from core.database_manager import database_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Действия перед запуском приложения
    # Создание таблиц в базе данных
    async with database_manager.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield
    # Действия после завершения приложения


app = FastAPI(
    lifespan=lifespan,
)
app.include_router(router=task_router)

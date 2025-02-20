from contextlib import asynccontextmanager

from fastapi import FastAPI
from api_v1 import router
from core.models import OrmBaseModel
from core.database_manager import database_manager
from core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Действия перед запуском приложения
    # Создание таблиц в базе данных
    async with database_manager.engine.begin() as connection:
        await connection.run_sync(OrmBaseModel.metadata.create_all)
    yield
    # Действия после завершения приложения


app = FastAPI(
    lifespan=lifespan,
)
# Добавление эндпоинтов в приложение
app.include_router(router=router)

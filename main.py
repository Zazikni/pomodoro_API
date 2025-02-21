from contextlib import asynccontextmanager

from fastapi import FastAPI
from api_v1 import router
from core.models import OrmBaseModel
from core.database_manager import database_manager
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Действия перед запуском приложения
    # Создание таблиц в базе данных
    async with database_manager.engine.begin() as connection:
        await connection.run_sync(OrmBaseModel.metadata.create_all)
    yield
    # Действия после завершения приложения
    await database_manager.dispose()


app = FastAPI(
    lifespan=lifespan,
)
# Добавление эндпоинтов в приложение
app.include_router(router=router)

if __name__ == "__main":
    import uvicorn

    uvicorn.run("main:app", host=settings.run.HOST, port=settings.run.PORT, reload=True)

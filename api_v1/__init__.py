__all__ = ("router",)
from fastapi import APIRouter
from .tasks.views import router as tasks_router

router = APIRouter(prefix="/api/v1")
router.include_router(router=tasks_router)

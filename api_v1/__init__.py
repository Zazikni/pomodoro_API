__all__ = ("router",)
from fastapi import APIRouter
from .tasks.views import router as tasks_router
from .users.views import router as users_router
from .categories.views import router as categories_router

router = APIRouter(prefix="/api/v1")
router.include_router(router=tasks_router)
router.include_router(router=users_router)
router.include_router(router=categories_router)

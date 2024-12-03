__all__ = ("routers",)
from .tasks.views import router as tasks_router

routers = [
    tasks_router,
]

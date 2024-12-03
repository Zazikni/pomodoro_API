from fastapi import FastAPI
from tasks.views import router as task_router

app = FastAPI()
app.include_router(router=task_router)

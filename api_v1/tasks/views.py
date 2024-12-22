from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.tasks.schemas import (
    Task,
    TaskCreate,
    TaskDelete,
    TaskUpdatePartial,
)
from .dependencies import get_task_by_id
from . import crud
from core.database_manager import database_manager

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get(
    "/all",
    response_model=list[Task],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Tasks not found"},
    },
    description="Endpoint to get all tasks",
)
async def get_tasks(
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
) -> list[Task]:
    return await crud.get_all_tasks(session=session)


@router.post(
    "/",
    response_model=Task,
)
async def create_task(
    task_data: TaskCreate,
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    return await crud.create_task(session=session, task=task_data)


@router.put(path="/edit", response_model=Task)
async def edit_task_partial(
    task_info: TaskUpdatePartial,
    task: Task = Depends(get_task_by_id),
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    new_task = await crud.edit_task_partial(
        session=session, new_task_data=task_info, task=task
    )
    return new_task


@router.delete(
    "/delete",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Task not found"},
    },
    description="Endpoint to delete a task",
)
async def delete_task(
    task: Task = Depends(get_task_by_id),
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    success = await crud.delete_task(session=session, task=task)
    if success:
        return {"message": f"Task with id: {task.id} successfully deleted"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Got some problems while deleting your task.",
    )

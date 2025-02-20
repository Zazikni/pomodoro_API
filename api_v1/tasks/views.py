from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.tasks.schemas import (
    Task,
    TaskCreate,
    TaskUpdatePartial,
)
from .dependencies import get_task_by_id_from_path
from . import crud
from core.database_manager import database_manager

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get(
    "/",
    response_model=list[Task],
    status_code=status.HTTP_200_OK,
    responses={},
    description="Endpoint to get all tasks",
)
async def get_tasks(
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    return await crud.get_all_tasks(session=session)


@router.post(
    "/",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
    description="Endpoint to create a new task",
    responses={},
)
async def create_task(
    task_data: TaskCreate,
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    return await crud.create_task(session=session, task=task_data)


@router.put(
    path="/{object_id}",
    response_model=Task,
    description="Endpoint to edit task",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Task not found"},
    },
)
async def edit_task_partial(
    task_info: TaskUpdatePartial,
    task: Task = Depends(get_task_by_id_from_path),
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    new_task = await crud.edit_task_partial(
        session=session, new_task_data=task_info, task=task
    )
    return new_task


@router.delete(
    "/{object_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Task not found"},
    },
    description="Endpoint to delete a task",
)
async def delete_task(
    task: Task = Depends(get_task_by_id_from_path),
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    await crud.delete_task(session=session, task=task)
    return

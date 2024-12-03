from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.tasks.schemas import Task, TaskCreate, TaskUpdateTitle, TaskDelete
from . import crud
from core.database_manager import database_manager

router = APIRouter(prefix="/tasks", tags=["tasks"])


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
    session: AsyncSession = Depends(database_manager.session_dependency),
) -> list[Task]:
    return await crud.get_all_tasks(session=session)


@router.post(
    "/",
    response_model=Task,
)
async def create_task(
    task_data: TaskCreate,
    session: AsyncSession = Depends(database_manager.session_dependency),
):
    return await crud.create_task(session=session, task=task_data)


@router.post(
    "/edit/title",
    response_model=Task,
)
async def edit_task_title(
    task_info: TaskUpdateTitle,
    session: AsyncSession = Depends(database_manager.session_dependency),
):
    success = await crud.edit_task_title(
        session=session, task_id=task_info.id, title=task_info.title
    )
    if success:
        return await crud.get_one_task(session=session, task_id=task_info.id)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with id: {task_info.id} not found",
    )


@router.delete(
    "/delete",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Task not found"},
    },
    description="Endpoint to get all tasks",
)
async def delete_task(
    task_info: TaskDelete,
    session: AsyncSession = Depends(database_manager.session_dependency),
):
    success = await crud.delete_task(session=session, task_id=task_info.id)
    if success:
        return {"message": f"Task with id: {task_info.id} successfully deleted"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with id: {task_info.id} not found",
    )

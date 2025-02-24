from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.tasks.schemas import TaskEdit
from core.database_manager import database_manager
from . import crud


async def get_task_by_id_from_path(
    object_id: int = Path(..., gt=0),
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    return await get_task_by_id(session=session, task_id=object_id)


async def get_task_by_id(
    task_id: int,
    session: AsyncSession,
):
    task = await crud.get_one_task(session=session, task_id=task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id: {task_id} not found",
        )

    return task

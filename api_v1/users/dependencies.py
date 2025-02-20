from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.users.schemas import UserEdit, UserCreate
from core.database_manager import database_manager
from . import crud


async def get_user_by_id_from_body(
    user_data: UserEdit,
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    return await get_user_by_id(session=session, user_id=user_data.id)


async def get_user_by_id_from_path(
    object_id: int = Path(..., gt=0),
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    return await get_user_by_id(session=session, user_id=object_id)


async def get_user_by_id(
    user_id: int,
    session: AsyncSession,
):
    user = await crud.get_user(session=session, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {user_id} not found",
        )

    return user

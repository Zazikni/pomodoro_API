from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.users.schemas import UserEdit
from core.database_manager import database_manager
from . import crud


async def get_user_by_id(
    user_data: UserEdit,
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    user = await crud.get_user(session=session, user_id=user_data.id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {user_data.id} not found",
        )

    return user

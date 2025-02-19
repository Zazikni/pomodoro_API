from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.users.schemas import User, UserEdit, UserCreate
from .dependencies import get_user_by_id
from core.database_manager import database_manager
from api_v1.users import crud


router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/",
    response_model=User,
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_404_NOT_FOUND: {"description": "User not found"}},
    description="Endpoint to get a user",
)
async def get_user(
    user: User = Depends(get_user_by_id),
):
    return user


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    # responses={status.HTTP_404_NOT_FOUND: {"description": "User not found"}},
    description="Endpoint to create user",
)
async def create_user(
    user: UserCreate,
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    user = await crud.create_user(session=session, user=user)
    return user


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={status.HTTP_404_NOT_FOUND: {"description": "User not found"}},
    description="Endpoint to delete user",
)
async def delete_user(
    user: User = Depends(get_user_by_id),
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    await crud.delete_user(session=session, user=user)
    return

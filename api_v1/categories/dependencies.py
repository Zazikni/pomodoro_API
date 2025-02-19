from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.categories.schemas import Category, CategoryCreate, CategoryEdit
from core.database_manager import database_manager
from . import crud


async def get_category_by_id_from_body(
    category_data: CategoryEdit,
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    category = await crud.get_category(session=session, category_id=category_data.id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id: {category_data.id} not found",
        )

    return category


async def get_category_by_id_from_path(
    category_id: int = Path(..., gt=0),
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    category = await get_category_by_id_from_body(
        category_data=CategoryEdit(id=category_id), session=session
    )

    return category

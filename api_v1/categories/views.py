from fastapi import APIRouter, status, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.categories.schemas import Category, CategoryEdit, CategoryCreate
from .dependencies import get_category_by_id_from_path, get_category_by_id_from_body
from core.database_manager import database_manager
from api_v1.categories import crud

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get(
    "/",
    response_model=list[Category],
    status_code=status.HTTP_200_OK,
    description="Endpoint to get all categories",
)
async def get_categories(
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    return await crud.get_all_categories(session=session)


@router.post(
    "/",
    response_model=Category,
    status_code=status.HTTP_200_OK,
    description="Endpoint to create category",
)
async def create_category(
    category: CategoryCreate,
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    return await crud.create_category(session=session, category=category)


@router.get(
    "/{category_id}",
    response_model=Category,
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_404_NOT_FOUND: {"description": "Category not found"}},
    description="Endpoint to get a category",
)
async def get_category(
    category: Category = Depends(get_category_by_id_from_path),
):
    return category


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Category not found"},
    },
    description="Endpoint to delete a category",
)
async def delete_category(
    category: Category = Depends(get_category_by_id_from_path),
    session: AsyncSession = Depends(database_manager.scoped_session_dependency),
):
    await crud.delete_category(session=session, category=category)
    return

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.models import OrmCategoryModel
from .schemas import CategoryCreate, Category


async def create_category(
    session: AsyncSession,
    category: CategoryCreate,
) -> OrmCategoryModel:
    new_category: OrmCategoryModel = OrmCategoryModel(**category.model_dump())
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)
    return new_category

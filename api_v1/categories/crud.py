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


async def delete_category(
    session: AsyncSession,
    category: OrmCategoryModel,
) -> None:
    await session.delete(category)
    await session.commit()


async def get_category(
    session: AsyncSession,
    category_id: int,
) -> OrmCategoryModel | None:
    return await session.get(OrmCategoryModel, category_id)


async def get_all_categories(session: AsyncSession) -> list[OrmCategoryModel]:
    statement = select(OrmCategoryModel).order_by(OrmCategoryModel.id)
    result: Result = await session.execute(statement)
    categories: list[OrmCategoryModel] = list(result.scalars().all())
    return categories


async def change_category_title(
    session: AsyncSession,
    category: OrmCategoryModel,
    new_title: str,
) -> OrmCategoryModel:
    category.title = new_title
    await session.commit()
    return category

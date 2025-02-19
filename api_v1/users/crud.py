from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.models import OrmUserModel
from .schemas import UserCreate, User


async def get_user(session: AsyncSession, user_id: int) -> OrmUserModel | None:
    user = await session.get(OrmUserModel, user_id)
    print(user)
    return user


async def create_user(session: AsyncSession, user: UserCreate) -> OrmUserModel:
    new_user: OrmUserModel = OrmUserModel(**user.model_dump())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


async def delete_user(session: AsyncSession, user: OrmUserModel) -> None:
    await session.delete(user)
    await session.commit()

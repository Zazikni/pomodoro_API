import sqlalchemy.exc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.models import OrmUserModel


async def get_user(session: AsyncSession, user_id: int) -> OrmUserModel | None:
    user = await session.get(OrmUserModel, user_id)
    print(user)
    return user

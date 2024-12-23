import sqlalchemy.exc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.models import User


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    user = await session.get(User, user_id)
    print(user)
    return user

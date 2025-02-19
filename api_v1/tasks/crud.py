import sqlalchemy.exc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.models import OrmTaskModel
from .schemas import TaskCreate, TaskUpdatePartial

from sqlalchemy.exc import SQLAlchemyError


async def get_all_tasks(session: AsyncSession) -> list[OrmTaskModel]:
    statement = select(OrmTaskModel).order_by(OrmTaskModel.id)
    result: Result = await session.execute(statement)
    tasks: list[OrmTaskModel] = list(result.scalars().all())
    return tasks


async def get_one_task(session: AsyncSession, task_id: int) -> OrmTaskModel | None:
    return await session.get(OrmTaskModel, task_id)


async def create_task(session: AsyncSession, task: TaskCreate) -> OrmTaskModel:
    new_task = OrmTaskModel(**task.model_dump())
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return new_task


async def delete_task(session: AsyncSession, task: OrmTaskModel) -> None:
    await session.delete(task)
    await session.commit()


async def edit_task_partial(
    session: AsyncSession, new_task_data: TaskUpdatePartial, task: OrmTaskModel
) -> OrmTaskModel:
    # new_task_data.model_dump(exclude_unset=True)
    for attr, value in new_task_data.model_dump(exclude_unset=True).items():
        setattr(task, attr, value)
    await session.commit()
    return task

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.models import Task
from .schemas import TaskCreate


async def get_all_tasks(session: AsyncSession) -> list[Task]:
    statement = select(Task).order_by(Task.id)
    result: Result = await session.execute(statement)
    tasks: list[Task] = list(result.scalars().all())
    return tasks


async def get_one_task(session: AsyncSession, task_id: int) -> Task | None:
    return await session.get(Task, task_id)


async def create_task(session: AsyncSession, task: TaskCreate) -> Task:
    new_task = Task(**task.model_dump())
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return new_task


async def delete_task(session: AsyncSession, task_id: int) -> bool:
    task = await get_one_task(session=session, task_id=task_id)
    if task:
        await session.delete(task)
        await session.commit()
        return True
    else:
        return False


async def edit_task_title(session: AsyncSession, task_id: int, title: str) -> bool:
    task = await get_one_task(session=session, task_id=task_id)
    if task:
        task.title = title
        await session.commit()
        return True
    else:
        return False

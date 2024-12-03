from typing import List

from fastapi import APIRouter, status, HTTPException
from api_v1.tasks.schemas import Task, TaskCreate, TaskUpdateTitle, TaskDelete

router = APIRouter(prefix="/tasks", tags=["tasks"])

default_task = Task(title="default_task_title", pomodoro_count=0, category_id=1, id=1)
default_tasks_list = [default_task]


@router.get(
    "/all",
    response_model=List[Task],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Tasks not found"},
    },
    description="Endpoint to get all tasks",
)
async def get_tasks():
    return default_tasks_list


@router.post(
    "/",
    response_model=Task,
)
async def create_task(task_data: TaskCreate):
    task = Task(
        title=task_data.title,
        pomodoro_count=task_data.pomodoro_count,
        category_id=task_data.category_id,
        id=len(default_tasks_list),
    )
    default_tasks_list.append(task)
    return task


@router.post(
    "/edit/title",
    response_model=Task,
)
async def edit_task_title(task_info: TaskUpdateTitle):
    for task in default_tasks_list:
        if task.id == task_info.id:
            task.title = task_info.title
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with id: {task_info.id} not found",
    )


@router.delete(
    "/delete",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Task not found"},
    },
    description="Endpoint to get all tasks",
    # response_model=Task,
)
async def delete_task(task_info: TaskDelete):
    for index, task in enumerate(default_tasks_list):
        if task.id == task_info.id:
            default_tasks_list.remove(task)
            return {"message": f"Task with id: {task_info.id} successfully deleted"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with id: {task_info.id} not found",
    )

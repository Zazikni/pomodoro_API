from typing import List

from fastapi import APIRouter, status, HTTPException
from api_v1.tasks.schemas import Task, tasks_fix

router = APIRouter(prefix="/tasks", tags=["tasks"])


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
    return tasks_fix


@router.post(
    "/",
    response_model=Task,
)
async def create_task(task_data: Task):
    print(task_data)
    tasks_fix.append(task_data)
    return task_data


@router.post(
    "/{task_id}",
    # response_model=Task,
)
async def edit_task_name(task_id: int):
    for task in tasks_fix:
        if task["id"] == task_id:
            task["title"] = "New Title"
            return {"data": task_id}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with id: {task_id} not found",
    )


@router.delete(
    "/{task_id}",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Task not found"},
    },
    description="Endpoint to get all tasks",
    # response_model=Task,
)
async def delete_task(task_id: int):
    for index, task in enumerate(tasks_fix):
        if task["id"] == task_id:
            del tasks_fix[index]
            return {"message": f"Task with id: {task_id} successfully deleted"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with id: {task_id} not found",
    )

from pydantic import BaseModel, Field


class Task(BaseModel):
    # id: int
    id: int = Field(exclude=True)  # Uncomment to exclude id field from the response
    title: str
    pomodoro_count: int
    category_id: int
    completed: bool = False


tasks_fix = [
    {
        "id": 1,
        "title": "Task 1",
        "pomodoro_count": 0,
        "category_id": 1,
        "completed": False,
    },
    {
        "id": 2,
        "title": "Task 2",
        "pomodoro_count": 0,
        "category_id": 2,
        "completed": False,
    },
    {
        "id": 3,
        "title": "Task 3",
        "pomodoro_count": 0,
        "category_id": 3,
        "completed": False,
    },
    {
        "id": 4,
        "title": "Task 4",
        "pomodoro_count": 0,
        "category_id": 1,
        "completed": False,
    },
    {
        "id": 5,
        "title": "Task 5",
        "pomodoro_count": 0,
        "category_id": 2,
        "completed": False,
    },
]

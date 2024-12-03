from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    # id: int = Field(exclude=True)  # Uncomment to exclude id field from the response
    pass


class TaskCreate(TaskBase):
    title: str
    pomodoro_count: int
    category_id: int


class Task(TaskBase):
    id: int
    title: str
    pomodoro_count: int
    category_id: int
    completed: bool = False


class TaskEditBase(TaskBase):
    id: int


class TaskUpdateTitle(TaskEditBase):
    title: str


class TaskUpdatePomodoroCount(TaskEditBase):
    pomodoro_count: int


class TaskUpdatePomodoroCategoryId(TaskEditBase):
    category_id: int


class TaskUpdatePomodoroCompleted(TaskEditBase):
    pass


class TaskDelete(TaskEditBase):
    pass

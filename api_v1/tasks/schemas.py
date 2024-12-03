from pydantic import BaseModel, Field, ConfigDict


class TaskBase(BaseModel):
    # id: int = Field(exclude=True)  # Uncomment to exclude id field from the response
    pass


class TaskCreate(TaskBase):
    title: str
    pomodoro_count: int
    category_id: int


class Task(TaskBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    pomodoro_count: int
    category_id: int
    completed: bool


class TaskEditBase(TaskBase):
    id: int


class TaskUpdateTitle(TaskEditBase):
    title: str


class TaskUpdatePartial(TaskEditBase):
    title: str | None = None
    pomodoro_count: int | None = None
    category_id: int | None = None


class TaskUpdatePomodoroCompleted(TaskEditBase):
    pass


class TaskDelete(TaskEditBase):
    pass

from sqlalchemy.orm import Mapped

from .base import Base


class Task(Base):
    title: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int]
    completed: Mapped[bool]

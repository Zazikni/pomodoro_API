from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Task(Base):
    title: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int]
    completed: Mapped[bool] = mapped_column(default=False)

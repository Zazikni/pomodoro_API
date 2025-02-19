from sqlalchemy.orm import Mapped, mapped_column

from .ormbasemodel import OrmBaseModel


class OrmTaskModel(OrmBaseModel):
    title: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int]
    completed: Mapped[bool] = mapped_column(default=False)

from sqlalchemy.orm import Mapped

from .base import Base


class User(Base):

    name: Mapped[str]
    surname: Mapped[str]

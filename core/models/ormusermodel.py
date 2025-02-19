from sqlalchemy.orm import Mapped

from .ormbasemodel import OrmBaseModel


class OrmUserModel(OrmBaseModel):

    name: Mapped[str]
    surname: Mapped[str]

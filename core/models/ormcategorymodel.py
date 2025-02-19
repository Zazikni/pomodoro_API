from sqlalchemy.orm import Mapped

from .ormbasemodel import OrmBaseModel


class OrmCategoryModel(OrmBaseModel):
    __tablename__ = "categories"
    name: Mapped[str]

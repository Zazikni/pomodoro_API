from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from core.config import settings


class OrmBaseModel(DeclarativeBase):
    __abstract__ = True  # Не будет создана таблица в БД
    metadata = MetaData(naming_convention=settings.database.NAMING_CONVENTIONS)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.replace("Orm", "", 1).replace("Model","",1).lower()}s"  # Имя таблицы будет именем модели в нижнем регистре

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

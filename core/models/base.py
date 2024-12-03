from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True  # Не будет создана таблица в БД

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"  # Имя таблицы будет именем модели в нижнем регистре

    id: Mapped[int] = mapped_column(primary_key=True)

from .base import Base


class Category(Base):
    __tablename__ = "categories"
    name: str

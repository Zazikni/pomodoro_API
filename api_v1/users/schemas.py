from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    pass


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    surname: str


class UserCreate(UserBase):
    name: str
    surname: str


class UserEdit(UserBase):
    id: int

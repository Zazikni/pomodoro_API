from pydantic import BaseModel, Field, ConfigDict


class CategoryBase(BaseModel):
    # id: int = Field(exclude=True)  # Uncomment to exclude id field from the response
    pass


class CategoryCreate(CategoryBase):
    title: str


class Category(CategoryBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str

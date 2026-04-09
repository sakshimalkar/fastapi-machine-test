from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str


class Category(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    name: str
    price: int
    category_id: int


class Product(BaseModel):
    id: int
    name: str
    price: int
    category_id: int
    category: Category

    class Config:
        orm_mode = True
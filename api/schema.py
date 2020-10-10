from datetime import datetime

from pydantic import BaseModel


class ArticleViewModel(BaseModel):
    id: int
    title: str
    addition_date: datetime
    photo: int
    text: str

    class Config:
        orm_mode = True


class PostArticleViewModel(BaseModel):
    title: str
    photo: int
    text: str

    class Config:
        orm_mode = True

class ProductViewModel(BaseModel):
    id: int
    title: str
    photo: int
    description: str
    price: float

    class Config:
        orm_mode = True


class PostProductViewModel(BaseModel):
    title: str
    photo: int
    description: str
    price: float

    class Config:
        orm_mode = True

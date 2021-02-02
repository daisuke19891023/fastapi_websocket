# schemas/user.py

# from datetime import datetime
from typing import List
from pydantic import BaseModel
from uuid import UUID
from .book import Book


class UserBase(BaseModel):
    username: str
    email: str


class User(UserBase):
    uuid: UUID
    hashed_password: UUID
    # 返す必要のない値は記述しなければ
    # レスポンスから切り捨てられる
    # created_at: datetime
    # updated_at: datetime

    # リレーションを張っている場合は
    # 書かないとバリデーションエラーになる
    class Config:
        orm_mode = True


class UserDetail(User):
    books: List[Book] = []


class UserCreate(UserBase):
    """Input"""
    password: str

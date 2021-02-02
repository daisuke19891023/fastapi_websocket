# user.py

from src.backend.database import Base
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin  # 後述


class User(Base, TimestampMixin):
    __tablename__ = 'users'

    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    username = Column(String(128), nullable=True)
    email = Column(String(128), nullable=True)
    hashed_password = Column(UUIDType(binary=False), default=uuid4)
    # リレーション設定
    # books = relationship(
    #     'Book',
    #     back_populates='user'
    # )

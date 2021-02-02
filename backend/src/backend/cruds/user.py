# cruds/user.py

from fastapi import HTTPException
from src.backend.models import User
from sqlalchemy.orm import Session
from src.backend.schemas.user import UserCreate as UserCreateSchema
from starlette.status import HTTP_404_NOT_FOUND
from uuid import UUID
# from src.backend.cruds.user import UserCreate
from hashlib import md5 as hash_func


def read_users(db: Session):
    items = db.query(User).all()
    return items


def read_user(db: Session, user_id: UUID):
    try:
        item = db.query(User).get(user_id)
    except BaseException:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')

    return item


def create_user_query(db: Session, user: UserCreateSchema):
    """create user by email and password"""
    hashed_password = hash_func(user.password.encode()).hexdigest()
    db_user = User(username=user.username,
                   email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

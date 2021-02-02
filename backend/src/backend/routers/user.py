# routers/user.py

import src.backend.cruds.user as crud
from src.backend.database import get_db
from fastapi import APIRouter, Depends
# schemas の中身は後述
from src.backend.schemas.user import \
    User as UserSchema, UserDetail as UserDetailSchema, UserCreate as UserCreateSchema
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

router = APIRouter()


# URL は /users 以降のみを書けばOK
@router.get('/', response_model=List[UserSchema])
async def read_users(db: Session = Depends(get_db)):
    return crud.read_users(db=db)


@router.get('/{user_id}', response_model=UserDetailSchema)
async def read_user(user_id: UUID, db: Session = Depends(get_db)):
    return crud.read_user(user_id=user_id, db=db)


@router.post("/create/", response_model=UserSchema)
async def create_user(user: UserCreateSchema,
                      db: Session = Depends(get_db)):

    return crud.create_user_query(db=db, user=user)

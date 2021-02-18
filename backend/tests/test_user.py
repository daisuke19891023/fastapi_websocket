from src.backend.database import get_db
from src.backend.main import app
from starlette.testclient import TestClient
import pytest
from sqlalchemy.orm import Session
from src.backend.models import User
from fastapi import APIRouter, Depends
from hashlib import md5 as hash_func


def temp_db(f):
    def func(SessionLocal, *args, **kwargs):
        # テスト用のDBに接続するためのsessionmaker instanse
        #  (SessionLocal) をfixtureから受け取る
        db = SessionLocal()

        def override_get_db():
            try:
                # db = SessionLocal()
                # hashed_password = hash_func(
                #     "hashed_password".encode()).hexdigest()
                # db_user = User(username="user.username",
                #                email="user.email", hashed_password=hashed_password)
                # db.add(db_user)
                # db.commit()
                yield db
            finally:
                db.close()

        # fixtureから受け取るSessionLocalを使うようにget_dbを強制的に変更
        app.dependency_overrides[get_db] = override_get_db
        # Run tests
        f(*args, **kwargs)
        # get_dbを元に戻す
        app.dependency_overrides[get_db] = get_db

    return func


def before_db(SessionLocal):
    db = SessionLocal()
    yield db


client = TestClient(app)


@temp_db
def test_create_user():
    response = client.post(
        "/users/create/", json={"username": "🤣", "email": "foo", "password": "fo"}
    )
    assert response.status_code == 200


@temp_db
def test_read_users_nothing():
    response = client.get(
        "/users/"
    )
    assert response.status_code == 200
    assert len(response.json()) == 0


@temp_db
def test_read_users(before_db):
    hashed_password = hash_func(
        "hashed_password".encode()).hexdigest()
    db_user = User(username="user.username",
                   email="user.email", hashed_password=hashed_password)
    before_db.add(db_user)
    before_db.commit()
    response = client.get(
        "/users/"
    )
    assert response.status_code == 200
    assert len(response.json()) == 1

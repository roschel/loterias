from sqlmodel import SQLModel, create_engine, Session

from config import settings
from schemas import *

SQLALCHEMY_DATABASE_URL = f"{settings.REPOSITORY_NAME}://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

session = Session(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from local_settings import DATABASE_URL


POSTGRESQL_DATABASE_URL = DATABASE_URL
if not POSTGRESQL_DATABASE_URL:
    raise ValueError("db not set")

engine = create_engine(POSTGRESQL_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db_session():
    return SessionLocal()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

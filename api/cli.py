from sqlalchemy_utils import database_exists, create_database
from database import engine, Base

def create_db():
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_db()
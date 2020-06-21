from app import db
from database.tables import Article

def create_tables():

    with db.connection_context():
        db.create_tables([
            not_existing_table for not_existing_table in [
                Article
            ] if not db.table_exists(not_existing_table)
        ])


if __name__ == '__main__':
    create_tables()

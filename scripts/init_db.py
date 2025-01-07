from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import ProgrammingError

DATABASE_URL = "sqlite:///./test.db"
DATABASE_NAME = "test.db"
OWNER = "user"


def initialize_database():
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

    try:
        with Session(engine) as session:
            session.execute("SELECT 1;")
        print(f"Database '{DATABASE_NAME}' initialized successfully.")
    except ProgrammingError as e:
        print(f"Error initializing database: {e}")


if __name__ == "__main__":
    initialize_database()
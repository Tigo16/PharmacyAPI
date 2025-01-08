from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from sqlalchemy.exc import ProgrammingError

DATABASE_URL = "sqlite:///./test.db"
DATABASE_NAME = "test.db"

def initialize_database():
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

    try:
        with Session(engine) as session:
            # Используем text для выполнения SQL-запроса
            session.execute(text("SELECT 1;"))
        print(f"Database '{DATABASE_NAME}' initialized successfully.")
    except ProgrammingError as e:
        print(f"Error initializing database: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    initialize_database()
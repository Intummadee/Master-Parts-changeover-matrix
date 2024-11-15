from sqlmodel import SQLModel
from app.database import engine
from app.models import Parts, Changeover

def run_migrations():
    print("Running migrations...")
    SQLModel.metadata.create_all(engine)
    print("Migrations complete!")

if __name__ == "__main__":
    run_migrations()

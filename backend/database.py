from datetime import datetime
from typing import Optional

# https://bugbytes.io/posts/setting-up-sqlmodel/

from sqlmodel import Field, SQLModel, create_engine, ForeignKey , Session

# There should be one engine for the entire application
DB_FILE = 'db.sqlite3'
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)



class Parts(SQLModel, table=True):
    __tablename__ = 'Parts'
    id: Optional[int] = Field(default=None, primary_key=True)
    part_name: str
    description: Optional[str] = None

class Changeover(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Primary key with auto-increment
    from_part_id: int = Field(foreign_key="Parts.id")  # Foreign key to parts table
    to_part_id: int = Field(foreign_key="Parts.id")  # Foreign key to parts table
    changeover_time: float

    class Config:
        unique_together = {"from_part_id", "to_part_id"}  # Unique constraint on from_part_id and to_part_id




def create_partsData():
    Parts_1 = Parts(name="TG1")
    Parts_2 = Parts(name="TG2")
    Parts_3 = Parts(name="TG3")

    session = Session(engine)

    session.add(Parts_1)
    session.add(Parts_2)
    session.add(Parts_3)

    session.commit()


def create_tables():
    SQLModel.metadata.create_all(engine)






def main():  
    create_tables()  
    # create_partsData()  


if __name__ == "__main__":  
    main()
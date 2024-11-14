from sqlalchemy import Column, Integer, String
from database import Base

class Part(Base):
    __tablename__ = "parts"
    id = Column(Integer, primary_key=True, index=True) # id column is defined as an integer and serves as the primary key
    name = Column(String, index=True)
    changeover_time = Column(Integer)

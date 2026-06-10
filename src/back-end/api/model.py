# api/model.py
from sqlalchemy import Column, Integer, String
from .database import Base

class Visit(Base):
    __tablename__ = "visits" # Name of the database table
    userid = Column(String, primary_key=True) # User ID
    count  = Column(Integer) # Number of visits
    
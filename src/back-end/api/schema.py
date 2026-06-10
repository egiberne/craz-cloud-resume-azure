# api/schemas.py
from pydantic import BaseModel

# Schema for creating a visit (input model)
class VisitCreate(BaseModel):
    userid: str
    count: int | None = None
# Schema for reading/returning a visit (output model)
class Visit(BaseModel):
    userid: str
    count: int | None = None
    class Config:
        # Enable ORM mode to allow Pydantic to read data from SQLAlchemy ORM objects
        orm_mode = True # For Pydantic v1.x
        # from_attributes = True # For Pydantic v2.x (use this if you have Pydantic v2+)
# api/main.py
from typing import List
from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session

from . import model, schema
from .database import engine, SessionLocal, Base
# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)
app = FastAPI()
# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Root endpoint for basic check
@app.get("/health")
def read_root():
    return {"message": "Welcome !"}



@app.post("/visit/", response_model=schema.Visit, status_code=status.HTTP_201_CREATED)
def set_visit(visit: schema.VisitCreate, db: Session = Depends(get_db)):
    db_visit = model.Visit(userid=visit.userid, count=visit.count + 1 if visit.count else 1)
    db.add(db_visit)
    db.commit()
    # db.refresh(db_visit)
    return db_visit
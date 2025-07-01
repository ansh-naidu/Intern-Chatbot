from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.database import SessionLocal
from app.models.training_module import TrainingModule

router = APIRouter()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/modules")
def get_modules(db: Session = Depends(get_db)):
    modules = db.query(TrainingModule).all()
    return modules

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.database import SessionLocal
from app.models.intern import Intern
from app.models.progress import Progress

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/interns")
def create_intern(name: str, email: str, db: Session = Depends(get_db)):
    intern = Intern(name=name, email=email)
    db.add(intern)
    db.commit()
    db.refresh(intern)
    return intern

@router.get("/interns")
def list_interns(db: Session = Depends(get_db)):
    return db.query(Intern).all()

@router.post("/progress/update")
def update_progress(intern_id: int, module_id: int, status: str, db: Session = Depends(get_db)):
    progress = db.query(Progress).filter_by(intern_id=intern_id, module_id=module_id).first()
    if progress:
        progress.status = status
    else:
        progress = Progress(intern_id=intern_id, module_id=module_id, status=status)
        db.add(progress)
    db.commit()
    return {"message": "Progress updated."}

@router.get("/progress/{intern_id}")
def get_progress(intern_id: int, db: Session = Depends(get_db)):
    return db.query(Progress).filter_by(intern_id=intern_id).all()

from fastapi import FastAPI
from app.utils.database import Base, engine
from app.models import training_module , intern , progress
from app.routes import modules , interns 


app = FastAPI()
# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to InternIQ API - FastAPI Running ✅"}

@app.get("/health")
def health_check():
    return {"status": "Running"}
app.include_router(modules.router)
app.include_router(interns.router)
from sqlalchemy import Column, Integer, String
from app.utils.database import Base

class TrainingModule(Base):
    __tablename__ = "training_modules"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    resource_link = Column(String)

from sqlalchemy import Column, Integer, String
from app.utils.database import Base

class Intern(Base):
    __tablename__ = "interns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

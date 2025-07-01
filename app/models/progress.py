from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.utils.database import Base

class Progress(Base):
    __tablename__ = "progress"

    id: Mapped[int] = mapped_column(primary_key=True)
    intern_id: Mapped[int] = mapped_column()
    module_id: Mapped[int] = mapped_column()
    status: Mapped[str] = mapped_column(String)

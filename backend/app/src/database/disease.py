from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class Disease(Base):
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column("name", String(length=255), unique=True, nullable=False)

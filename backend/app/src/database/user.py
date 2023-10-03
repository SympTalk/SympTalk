from datetime import datetime

from sqlalchemy import func, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class User(Base):
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    account: Mapped[str] = mapped_column("account", String(length=255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column("password", String(length=255), nullable=False)
    birth_date: Mapped[datetime] = mapped_column("age", Integer, nullable=False)
    nickname: Mapped[str] = mapped_column("nickname", String(length=255), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        "created_at",
        DateTime(timezone=True),
        default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column("updated_at", DateTime(timezone=True), nullable=True)
    deleted_at: Mapped[datetime] = mapped_column("deleted_at", DateTime(timezone=True), nullable=True)

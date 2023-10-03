from datetime import datetime

from sqlalchemy import func, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.constant import DatabaseForeignKeyConstraint
from src.database.base import Base


class UserQuestion(Base):
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id: Mapped[int] = mapped_column(
        "user_id",
        ForeignKey(
            "user.id",
            onupdate=DatabaseForeignKeyConstraint.CASCACDE.value,
            ondelete=DatabaseForeignKeyConstraint.SET_NULL.value,
        ),
        nullable=True
    )
    content: Mapped[str] = mapped_column("content", String(length=255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        "created_at",
        DateTime(timezone=True),
        default=func.now(),
        nullable=False,
    )
from datetime import datetime

from sqlalchemy import func, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.constant import DatabaseForeignKeyConstraint
from src.database.base import Base


class UserAnswer(Base):
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    question_id: Mapped[int] = mapped_column(
        "question_id",
        ForeignKey(
            "user_question.id",
            onupdate=DatabaseForeignKeyConstraint.CASCACDE.value,
            ondelete=DatabaseForeignKeyConstraint.RESTRICT.value,
        ),
        nullable=False
    )
    content: Mapped[str] = mapped_column("content", String(length=255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        "created_at",
        DateTime(timezone=True),
        default=func.now(),
        nullable=False,
    )    

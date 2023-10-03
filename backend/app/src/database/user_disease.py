from datetime import datetime

from sqlalchemy import func, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.constant import DatabaseForeignKeyConstraint
from src.database.base import Base


class UserDisease(Base):
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id: Mapped[int] = mapped_column(
        "user_id",
        ForeignKey(
            "user.id",
            onupdate=DatabaseForeignKeyConstraint.CASCACDE.value,
            ondelete=DatabaseForeignKeyConstraint.SET_NULL.value,
        ),
        nullable=True
    ),
    disease_id: Mapped[int] = mapped_column(
        "disease_id",
        ForeignKey(
            "disease.id",
            onupdate=DatabaseForeignKeyConstraint.CASCACDE.value,
            ondelete=DatabaseForeignKeyConstraint.RESTRICT.value,
        ),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        "created_at",
        DateTime(timezone=True),
        default=func.now(),
        nullable=False,
    )


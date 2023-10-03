from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.constant import DatabaseForeignKeyConstraint
from src.database.base import Base


class UserAnswerSymptom(Base):
    answer_id: Mapped[int] = mapped_column(
        "answer_id",
        Integer,
        ForeignKey(
            "user_answer.id",
            onupdate=DatabaseForeignKeyConstraint.CASCACDE.value,
            ondelete=DatabaseForeignKeyConstraint.RESTRICT.value,            
        ),
        primary_key=True,
        nullable=False
    )
    symptom_id: Mapped[int] = mapped_column(
        "symptom_id",
        Integer,
        ForeignKey(
            "symptom.id",
            onupdate=DatabaseForeignKeyConstraint.CASCACDE.value,
            ondelete=DatabaseForeignKeyConstraint.RESTRICT.value,
        ),
        primary_key=True,
        nullable=False
    )

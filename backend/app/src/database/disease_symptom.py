from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.constant import DatabaseForeignKeyConstraint
from src.database.base import Base


class DiseaseSymptom(Base):
    disease_id: Mapped[int] = mapped_column(
        "disease_id",
        Integer,
        ForeignKey(
            "disease.id",
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

from enum import Enum


class DatabaseForeignKeyConstraint(str, Enum):
    SET_NULL: str = "SET NULL"
    RESTRICT: str = "RESTRICT"
    CASCACDE: str = "CASCADE"

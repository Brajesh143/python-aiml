from database import Base
from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column

class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    department: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    salary: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )
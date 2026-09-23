from database import Base
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column 

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    password: Mapped[str] = mapped_column(
        String(250)
    )

    role: Mapped[str] = mapped_column(
        String(30)
    )

    isActive: Mapped[bool] = mapped_column(
        Boolean
    )




from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String

from app.db import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        nullable=False,
        unique=True,
        primary_key=True
    )
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50))
    hashed_password: Mapped[str]
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)
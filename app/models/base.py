from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import mapped_column, Mapped
# from sqlalchemy import String

class Base(DeclarativeBase):    
    pass
#
# class Users(Base):
#     __tablename__ = 'users'

#     id: Mapped[int] = mapped_column(
#         autoincrement=True,
#         nullable=False,
#         unique=True,
#         primary_key=True
#     )
#     first_name: Mapped[str] = mapped_column(String(30))
#     last_name: Mapped[str] = mapped_column(String(30))
#     email: Mapped[str] = mapped_column(String(50))
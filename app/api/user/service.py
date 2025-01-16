from typing import AsyncIterator
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select, ScalarResult
from app.models import User


class UserService:
    session: AsyncSession = None

    def __init__(self, session: AsyncSession):
        self.session = session

    @classmethod
    async def create(cls, user: User) -> User:
        cls.session.add(user)
        await cls.session.flush()

        new: User = await cls.read(user.id)
        if not new:
            raise RuntimeError()
        return new

    @classmethod
    async def read(cls, user_id: int) -> User:
        stmt = select(User).where(User.id == user_id)
        return await cls.session.scalar(stmt.order_by(User.id))

    @classmethod
    async def read_all(cls):
        stmt = select(User)
        users = await cls.session.scalars(stmt.order_by(User.id))
        return users.all()


    @classmethod
    async def update(cls, user_id: int, user: User) -> User:
        user_to_update: User = await cls.read(user_id)
        if not user_to_update:
            raise RuntimeError()

        user_to_update.first_name = user.first_name
        user_to_update.last_name = user.last_name
        user_to_update.email = user.email
        user_to_update.is_superuser = user.is_superuser
        user_to_update.is_active = user.is_active

        await cls.session.flush()
        return user_to_update

    @classmethod
    async def delete(cls, user_id: int):
        user_to_delete: User = await cls.read(user_id)
        if not user_to_delete:
            raise RuntimeError()
        await cls.session.delete(user_to_delete)
        await cls.session.flush()

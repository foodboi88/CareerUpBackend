from uuid import uuid4

from sqlalchemy import Column, DateTime, String, Text, insert

from .base import Base, Crud


class UserInfoCrud(Crud, Base):
    __tablename__ = "user_info"

    id = Column(String(255), primary_key=True)
    user_name = Column(String(255), unique=True, nullable=False)
    user_type = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255))
    created_date = Column(DateTime)
    last_modified_date = Column(DateTime)
    description = Column(Text)

    @classmethod
    async def create(cls, attrs: dict):
        id = str(uuid4())
        attrs["id"] = id
        attrs["user_type"] = "0"
        await cls.execute(insert(cls).values(**attrs))
        return id

    @classmethod
    async def find_by_username(cls, username: str):
        return await cls.fetch_one(cls.select().where(cls.user_name == username))

    @classmethod
    async def find_by_email(cls, email: str):
        return await cls.fetch_one(cls.select().where(cls.email == email))

    @classmethod
    async def exists_by_username(cls, username: str):
        return await cls.find_by_username(username) is not None

    @classmethod
    async def exists_by_email(cls, email: str):
        return await cls.find_by_email(email) is not None

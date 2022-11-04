from os import getenv

from databases import Database
from sqlalchemy import select as _select
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.sql import Select
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = getenv("DATABASE_URL", "sqlite+aiosqlite:///database.db")
engine = create_async_engine(DATABASE_URL)
Base = declarative_base()

class Crud:

    @classmethod
    async def execute(cls, stmt: str):
        async with Database(DATABASE_URL) as db:
            return await db.execute(stmt)

    @classmethod
    async def fetch_one(cls, stmt: str):
        async with Database(DATABASE_URL) as db:
            return await db.fetch_one(stmt)

    @classmethod
    async def fetch_all(cls, stmt: str):
        async with Database(DATABASE_URL) as db:
            return await db.fetch_all(stmt)

    @classmethod
    async def fetch_val(cls, stmt: str):
        async with Database(DATABASE_URL) as db:
            return await db.fetch_val(stmt)

    @classmethod
    def select(cls) -> Select:
        return _select(cls)

    @classmethod
    async def find_by_id(cls, id):
        return await cls.fetch_one(cls.select().where(cls.id == id))

    @classmethod
    async def find_all(cls, limit: int, offset: int):
        return await cls.fetch_all(cls.select().limit(limit).offset(offset))

    @classmethod
    async def find_all_no_limit(cls):
        return await cls.fetch_all(cls.select())

    @classmethod
    async def find_all_by_attr(cls, attr, value, limit: int, offset: int):
        return await cls.fetch_all(cls.select().where(attr == value).limit(limit).offset(offset))

    @classmethod
    async def find_all_by_attr_no_limit(cls, attr, value):
        return await cls.fetch_all(cls.select().where(attr == value))

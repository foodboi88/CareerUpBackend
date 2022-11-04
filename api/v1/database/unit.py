from sqlalchemy import Column, ForeignKey, String

from .base import Base, Crud


class UnitCrud(Crud, Base):
    __tablename__ = "unit"

    id = Column(String(255), primary_key=True)
    unit_name = Column(String(255))
    subjects_id = Column(String(255), ForeignKey("subjects.id"))

    @classmethod
    async def find_by_unit_name(cls, unit_name: str):
        return await cls.fetch_one(cls.select().where(cls.unit_name.contains(unit_name)))

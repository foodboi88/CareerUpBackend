from sqlalchemy import Column, Float, ForeignKey, String

from .base import Base, Crud


class MarkUnitCrud(Crud, Base):
    __tablename__ = "mark_unit"

    id = Column(String(255), primary_key=True)
    mark_unit_name = Column(String(255))
    mark = Column(Float)
    unit_id = Column(String(255), ForeignKey("unit.id"))
    specialized_of_school_id = Column(String(255), ForeignKey("specialized_of_school.id"))

    @classmethod
    async def find_all_by_mark_below_and_unit_id_and_specialized_of_school_id(cls, mark: float, unit_id: str, specialized_of_school_id: str):
        return await cls.fetch_all(
            cls.select()
                .where(cls.mark <= mark)
                .where(cls.unit_id == unit_id)
                .where(cls.specialized_of_school_id == specialized_of_school_id)
        )

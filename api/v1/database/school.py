from sqlalchemy import Column, Float, ForeignKey, String, Text
from sqlalchemy.sql.functions import func

from .specialized_of_school import SpecializedOfSchoolCrud
from .mark_unit import MarkUnitCrud
from .base import Base, Crud


class SchoolCrud(Crud, Base):
    __tablename__ = "school"

    id = Column(String(255), primary_key=True)
    school_name = Column(String(255))
    school_short_name = Column(String(255))
    school_description = Column(Text)
    school_logo = Column(String(255))
    school_number_of_student = Column(String(255))
    school_rank = Column(Float)
    area_id = Column(String(255), ForeignKey("area.id"))

    @classmethod
    async def find_all_by_area_id(cls, area_id: str, limit: int, offset: int):
        return await cls.find_all_by_attr(cls.area_id, area_id, limit, offset)

    @classmethod
    async def find_all_by_specialized_id_and_mark_and_unit_ids(cls, specialized_id: str, mark: float, unit_ids: list[str]):
        return await cls.fetch_all(
            cls.select()
                .join(SpecializedOfSchoolCrud)
                .join(MarkUnitCrud)
                .where(SpecializedOfSchoolCrud.specialized_id == specialized_id)
                .where(MarkUnitCrud.mark <= mark)
                .where(MarkUnitCrud.unit_id.in_(unit_ids))
                .order_by(MarkUnitCrud.mark.desc())
                .distinct()
        )

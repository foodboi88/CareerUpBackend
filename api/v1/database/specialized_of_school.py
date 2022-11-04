from sqlalchemy import Column, ForeignKey, String, Text

from .base import Base, Crud
from .mark_unit import MarkUnitCrud
from .unit import UnitCrud


class SpecializedOfSchoolCrud(Crud, Base):
    __tablename__ = "specialized_of_school"

    id = Column(String(255), primary_key=True)
    specialized_of_school_name = Column(String(255))
    specialized_of_school_description = Column(Text)
    specialized_of_school_code = Column(String(255))
    specialized_of_school_year = Column(String(255))
    kpi = Column(String(255))
    way = Column(String(255))
    advice = Column(String(255))
    status = Column(String(255))
    fee = Column(String(255))
    school_id = Column(String(255), ForeignKey("school.id"))
    specialized_id = Column(String(255), ForeignKey("specialized.id"))

    @classmethod
    async def find_all_by_specialized_id(cls, specialized_id: str):
        return await cls.find_all_by_attr_no_limit(cls.specialized_id, specialized_id)

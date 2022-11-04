from sqlalchemy import Column, String, Text

from .base import Base, Crud


class BranchCrud(Crud, Base):
    __tablename__ = "branch"

    id = Column(String(255), primary_key=True)
    branch_name = Column(String(255))
    branch_description = Column(Text)
    branch_average_wage = Column(String(255))
    branch_suitable_personality = Column(String(255))
    branch_advice = Column(String(255))

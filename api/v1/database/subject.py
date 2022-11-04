from sqlalchemy import Column, String

from .base import Base, Crud


class SubjectCrud(Crud, Base):
    __tablename__ = "subjects"

    id = Column(String(255), primary_key=True)
    subjects_name = Column(String(255))

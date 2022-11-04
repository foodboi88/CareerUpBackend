from sqlalchemy import Column, String, Text

from .base import Base, Crud


class AreaCrud(Crud, Base):
    __tablename__ = "area"

    id = Column(String(255), primary_key=True)
    area_name = Column(String(255))
    area_description = Column(Text)

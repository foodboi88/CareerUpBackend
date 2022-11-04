from sqlalchemy import Column, String, Text

from .base import Base, Crud


class QuestionCrud(Crud, Base):
    __tablename__ = "question"

    id = Column(String(255), primary_key=True)
    content = Column(Text)
    personality = Column(Text)

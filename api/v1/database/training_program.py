from sqlalchemy import Column, ForeignKey, String, Integer

from .base import Base, Crud


class TrainingProgramCrud(Crud, Base):
    __tablename__ = "training_program"

    id = Column(String(255), primary_key=True)
    training_program_name = Column(String(255))
    credits = Column(Integer)
    specialized_id = Column(String(255), ForeignKey("specialized.id"))

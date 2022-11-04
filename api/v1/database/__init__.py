__all__ = (
    "AreaCrud",
    "BranchCrud",
    "MarkUnitCrud",
    "QuestionCrud",
    "SchoolCrud",
    "SpecializedCrud",
    "SpecializedOfSchoolCrud",
    "SubjectCrud",
    "TrainingProgramCrud",
    "UnitCrud",
    "UserInfoCrud",
    "create_tables",
)

from .area import AreaCrud
from .branch import BranchCrud
from .mark_unit import MarkUnitCrud
from .question import QuestionCrud
from .school import SchoolCrud
from .specialized import SpecializedCrud
from .specialized_of_school import SpecializedOfSchoolCrud
from .subject import SubjectCrud
from .training_program import TrainingProgramCrud
from .unit import UnitCrud
from .user_info import UserInfoCrud


async def create_tables():
    from .base import Base, engine
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

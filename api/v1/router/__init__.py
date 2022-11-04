__all__ = (
    "area_router",
    "auth_router",
    "branch_router",
    "question_router",
    "school_router",
    "specialized_router",
    "unit_router",
    "user_router",
)

from .area import area_router
from .auth import auth_router
from .branch import branch_router
from .question import question_router
from .school import school_router
from .specialized import specialized_router
from .unit import unit_router
from .user import user_router

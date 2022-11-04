from fastapi import APIRouter, Depends

from ..database import BranchCrud, SpecializedCrud
from ..middleware.auth import require_existed
from ..schema.branch import Branch
from ..schema.specialized import Specialized

branch_router = APIRouter()


@branch_router.get("", response_model=list[Branch], tags=["Branch"])
async def read_all_branchs(limit: int = 10, offset: int = 0):
    return await BranchCrud.find_all(limit=limit, offset=offset)


@branch_router.get("/{id}", response_model=Branch, tags=["Branch"])
async def read_branch_by_id(branch = Depends(require_existed(BranchCrud))):
    return branch


@branch_router.get("/{id}/specialized", response_model=list[Specialized], tags=["Branch", "Specialized"])
async def read_specializeds_by_branch_id(limit: int = 10, offset: int = 0, branch = Depends(require_existed(BranchCrud))):
    return await SpecializedCrud.find_all_by_branch_id(branch.id, limit, offset)

from fastapi import APIRouter, Depends

from ..database import SpecializedCrud
from ..middleware.auth import require_existed
from ..schema.specialized import Specialized

specialized_router = APIRouter()


@specialized_router.get("", response_model=list[Specialized], tags=["Specialized"])
async def read_all_specializeds(limit: int = 10, offset: int = 0):
    return await SpecializedCrud.find_all(limit=limit, offset=offset)


@specialized_router.get("/{id}", response_model=Specialized, tags=["Specialized"])
async def read_specialized_by_id(specialized = Depends(require_existed(SpecializedCrud))):
    return specialized


@specialized_router.get("/{id}/similar", response_model=list[Specialized], tags=["Specialized"])
async def read_similar_specializeds(specialized = Depends(require_existed(SpecializedCrud))):
    return await SpecializedCrud.find_all_by_cluster_and_branch_id(specialized.cluster, specialized.branch_id, specialized.id)

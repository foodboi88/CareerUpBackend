from fastapi import APIRouter, Depends

from ..database import UnitCrud
from ..middleware.auth import require_existed
from ..schema.unit import Unit

unit_router = APIRouter()


@unit_router.get("", response_model=list[Unit], tags=["Unit"])
async def read_all_units(limit: int = 10, offset: int = 0):
    return await UnitCrud.find_all(limit=limit, offset=offset)


@unit_router.get("/{id}", response_model=Unit, tags=["Unit"])
async def read_unit_by_id(unit = Depends(require_existed(UnitCrud))):
    return unit

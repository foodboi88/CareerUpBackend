from fastapi import APIRouter, Depends

from ..database import AreaCrud, SchoolCrud
from ..middleware.auth import require_existed
from ..schema.area import Area
from ..schema.school import School

area_router = APIRouter()


@area_router.get("", response_model=list[Area], tags=["Area"])
async def read_all_areas(limit: int = 10, offset: int = 0):
    return await AreaCrud.find_all(limit=limit, offset=offset)


@area_router.get("/{id}", response_model=Area, tags=["Area"])
async def read_area_by_id(area = Depends(require_existed(AreaCrud))):
    return area


@area_router.get("/{id}/school", response_model=list[School], tags=["Area", "School"])
async def read_schools_by_area_id(limit: int = 10, offset: int = 0, area = Depends(require_existed(AreaCrud))):
    return await SchoolCrud.find_all_by_area_id(area.id, limit, offset)

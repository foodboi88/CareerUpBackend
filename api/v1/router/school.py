from fastapi import APIRouter, Depends

from ..database import (MarkUnitCrud, SchoolCrud, SpecializedOfSchoolCrud,
                        UnitCrud, SubjectCrud)
from ..exception.http import ValidationException
from ..middleware.auth import require_existed
from ..schema.school import School, SpecializedOfSchool


async def parse_unit_names(unit_names: str) -> list[UnitCrud]:
    units = []
    for unit_name in unit_names.split(","):
        unit = await UnitCrud.find_by_unit_name(unit_name)
        if unit is None:
            raise ValidationException(f"unit_name {unit_name} is not found")
        units.append(unit)
    return units


school_router = APIRouter()


@school_router.get("", response_model=list[School], tags=["School"])
async def read_all_schools(limit: int = 10, offset: int = 0):
    return await SchoolCrud.find_all(limit=limit, offset=offset)


# @school_router.get("/search", response_model=list[School], tags=["School"])
@school_router.get("/search", response_model=list[SpecializedOfSchool], tags=["School"])
async def search_schools(
    specialized_id: str,
    mark: float,
    units: list[UnitCrud] = Depends(parse_unit_names),
):
    # return await SchoolCrud.find_all_by_specialized_id_and_mark_and_unit_ids(specialized_id, mark, [unit.id for unit in units])
    return sorted(
        [
            {
                **specialized_of_school,
                "school": await SchoolCrud.find_by_id(specialized_of_school.school_id),
                "units": ret_units,
            }
            for specialized_of_school in await SpecializedOfSchoolCrud.find_all_by_specialized_id(specialized_id)
            if len(
                ret_units := [
                    {
                        **unit,
                        "subject": await SubjectCrud.find_by_id(unit.subjects_id),
                        "mark_units": mark_units
                    }
                    for unit in units
                    if len(
                        mark_units := await MarkUnitCrud.find_all_by_mark_below_and_unit_id_and_specialized_of_school_id(
                            mark,
                            unit.id,
                            specialized_of_school.id,
                        )
                    ) > 0
                ]
            ) > 0
        ],
        key=lambda specialized_of_school: specialized_of_school["units"][0]["mark_units"][0]["mark"],
        reverse=True,
    )


@school_router.get("/{id}", response_model=School, tags=["School"])
async def read_school_by_id(school = Depends(require_existed(SchoolCrud))):
    return school

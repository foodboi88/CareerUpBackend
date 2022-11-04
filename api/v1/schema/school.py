from pydantic import BaseModel


class School(BaseModel):
    id: str
    school_name: str | None
    school_short_name: str | None
    school_description: str | None
    school_logo: str | None
    school_number_of_student: str | None
    school_rank: float | None
    area_id: str | None


class Subject(BaseModel):
    id: str
    subjects_name: str | None


class MarkUnit(BaseModel):
    id: str
    mark_unit_name: str | None
    mark: float | None


class Unit(BaseModel):
    id: str
    unit_name: str | None
    subject: Subject | None
    mark_units: list[MarkUnit]


class SpecializedOfSchool(BaseModel):
    id: str
    specialized_of_school_name: str | None
    specialized_of_school_description: str | None
    specialized_of_school_code: str | None
    specialized_of_school_year: str | None
    kpi: str | None
    way: str | None
    advice: str | None
    status: str | None
    fee: str | None
    school: School | None
    units: list[Unit]

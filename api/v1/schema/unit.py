from pydantic import BaseModel


class Unit(BaseModel):
    id: str
    unit_name: str | None
    subjects_id: str | None

from pydantic import BaseModel


class Area(BaseModel):
    id: str
    area_name: str | None
    area_description: str | None

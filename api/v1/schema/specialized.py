from pydantic import BaseModel


class Specialized(BaseModel):
    id: str
    specialized_name: str | None
    specialized_description: str | None
    personality_type_id: str | None
    cluster: int | None
    branch_id: str | None

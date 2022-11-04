from pydantic import BaseModel


class Branch(BaseModel):
    id: str
    branch_name: str | None
    branch_description: str | None
    branch_average_wage: str | None
    branch_suitable_personality: str | None
    branch_advice: str | None

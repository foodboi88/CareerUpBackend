from pydantic import BaseModel, validator

from .specialized import Specialized


class Question(BaseModel):
    id: int
    content: str


class Answer(BaseModel):
    question_id: int
    score: int

    @validator("score")
    def score_must_be_between_1_and_4(cls, score):
        if score not in range(1, 5):
            raise ValueError("Score must be between 1 and 4")
        return score


class TestResult(BaseModel):
    personality: str
    score: int
    specializeds: list[Specialized]

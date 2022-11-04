from fastapi import APIRouter

from ..schema.question import Question, Answer, TestResult
from ..database import QuestionCrud, SpecializedCrud

question_router = APIRouter()


@question_router.get("", response_model=list[Question], tags=["Question"])
async def read_all_questions():
    return await QuestionCrud.find_all_no_limit()


@question_router.post("", response_model=list[TestResult], tags=["Question"])
async def get_test_result(data: list[Answer]):
    scores = {}
    for answer in data:
        question = await QuestionCrud.find_by_id(answer.question_id)
        personality = question.personality
        if personality not in scores:
            scores[personality] = 0
        scores[personality] += answer.score
    return sorted(
        [
            {
                "personality": personality,
                "score": scores[personality],
                "specializeds": await SpecializedCrud.find_all_by_personality(personality),
            }
            for personality in scores
        ],
        key=lambda x: x["score"],
        reverse=True,
    )

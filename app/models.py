from pydantic import BaseModel


class QuestionIn(BaseModel):
    question: str


class SourceOut(BaseModel):
    document: str
    preview: str


class AnswerOut(BaseModel):
    answer: str
    sources: list[SourceOut]

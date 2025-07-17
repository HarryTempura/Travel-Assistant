import operator
from typing import TypedDict, Annotated


class PlanState(TypedDict):
    location: str
    questions: list[str]
    answers: list[str]
    request: Annotated[list[str], operator.add]

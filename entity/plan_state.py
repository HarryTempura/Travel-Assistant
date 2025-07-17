from typing import TypedDict


class PlanState(TypedDict):
    location: str
    ques_answer:dict[str,str]
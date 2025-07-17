from typing import List

from pydantic import BaseModel, Field


class Questions(BaseModel):
    question: List[str] = Field(description='要和用户确认的问题')

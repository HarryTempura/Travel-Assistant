from pydantic import BaseModel, Field


class Requests(BaseModel):
    location: str = Field(description='目的地')
    departure: str = Field(description='出发地')
    departure_time: str = Field(description='出发时间')
    return_time: str = Field(description='返回时间')
    trip_style: str = Field(description='行程风格，松散一些或者是紧张一些')
    trip_theme: str = Field(description='行程主题，人文、自然、美食等')
    attractions: str = Field(description='此行必去的景点，必须安排到行程中')
    budget: str = Field(description='本次行程的预算，含机酒')

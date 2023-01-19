from typing import List

from pydantic import BaseModel


class NewsBase(BaseModel):
    news: str
    url: str
    time: str
    sport: str


class News(NewsBase):
    news_id: str


class NewsList(BaseModel):
    news: List[News]
    
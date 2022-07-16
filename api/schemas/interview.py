import datetime
from typing import Optional

from pydantic import BaseModel, Field


class InterviewBase(BaseModel):
    content: Optional[str] = Field(None, example='これまで開発したもので一番自信があるものはなんですか')


class Interview(InterviewBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True


class InterviewCreate(InterviewBase):
    pass


class InterviewCreateResponse(InterviewCreate):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True


class BookmarkInterview(BaseModel):
    interview_id: int


class BookmarkInterviewCreate(BookmarkInterview):
    pass


class BookmarkInterviewDelete(BookmarkInterview):
    pass


class BookmarkInterviewCreateResponse(BookmarkInterviewCreate):
    user_id: int

    class Config:
        orm_mode = True

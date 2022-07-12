import datetime
from typing import List

from fastapi import APIRouter

import api.schemas.interview as interview_schema

router = APIRouter()


@router.post('/interview', response_model=interview_schema.InterviewCreateResponse)
async def create_interview(interview_body: interview_schema.InterviewCreate):
    return interview_schema.InterviewCreateResponse(
        id=1,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
        **interview_body.dict()
    )


@router.get('/interview/random', response_model=List[interview_schema.Interview])
async def obtain_random_interviews():
    return [interview_schema.Interview(id=1, content='これまで開発したもので一番自信があるものはなんですか')]


@router.get('/interview/bookmark', response_model=List[interview_schema.Interview])
async def obtain_bookmarked_interviews():
    return [interview_schema.Interview(id=1, content='これまで開発したもので一番自信があるものはなんですか')]


@router.post('/interview/bookmark', response_model=interview_schema.BookmarkInterviewCreateResponse)
async def add_bookmark_interview(bookmark_body: interview_schema.BookmarkInterviewCreate):
    return interview_schema.BookmarkInterviewCreateResponse(
        user_id=1,
        **bookmark_body.dict()
    )


@router.delete('/interview/bookmark')
async def delete_bookmark_interview():
    pass

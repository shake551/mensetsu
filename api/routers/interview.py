from typing import List

from fastapi import APIRouter

import api.schemas.interview as interview_schema

router = APIRouter()


@router.post('/interview')
async def create_interview():
    pass


@router.get('/interview/random', response_model=List[interview_schema.Interview])
async def obtain_random_interviews():
    return [interview_schema.Interview(id=1, content='これまで開発したもので一番自信があるものはなんですか')]


@router.get('/interview/bookmark', response_model=List[interview_schema.Interview])
async def obtain_bookmarked_interviews():
    return [interview_schema.Interview(id=1, content='これまで開発したもので一番自信があるものはなんですか')]


@router.post('/interview/bookmark')
async def add_bookmark_interview():
    pass


@router.delete('/interview/bookmark')
async def delete_bookmark_interview():
    pass

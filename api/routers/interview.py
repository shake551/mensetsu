import datetime
from typing import List

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import api.repository.interview as interview_repository
from api.db import get_db

import api.schemas.interview as interview_schema

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post('/interview', response_model=interview_schema.Interview)
def create_interview(
        interview_body: interview_schema.InterviewCreate,
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme),
):
    return interview_repository.create_interview(db=db, interview_create=interview_body, token=token)


@router.get('/interview/random', response_model=List[interview_schema.Interview])
async def obtain_random_interviews(
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme),
):
    return interview_repository.obtain_random_interviews(db=db, token=token)


@router.get('/interview/bookmark', response_model=List[interview_schema.Interview])
async def obtain_bookmarked_interviews():
    now = datetime.datetime.now()

    return [
        interview_schema.Interview(id=1, content='これまで開発したもので一番自信があるものはなんですか', created_at=now, updated_at=now),
        interview_schema.Interview(id=2, content='使用技術を選択した理由はなんですか', created_at=now, updated_at=now),
        interview_schema.Interview(id=3, content='こだわったポイントはどこですか', created_at=now, updated_at=now),
        interview_schema.Interview(id=4, content='一番難しかったことはなんですか', created_at=now, updated_at=now),
        interview_schema.Interview(id=5, content='今後改善したいところはありますか', created_at=now, updated_at=now)
    ]


@router.post('/interview/bookmark', response_model=interview_schema.BookmarkInterviewCreateResponse)
async def add_bookmark_interview(
        bookmark_body: interview_schema.BookmarkInterviewCreate,
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme),
):
    return interview_repository.bookmark_interviews(
        bookmark_request=bookmark_body,
        db=db,
        token=token,
    )


@router.delete('/interview/bookmark')
async def delete_bookmark_interview(bookmark_body: interview_schema.BookmarkInterviewDelete):
    pass

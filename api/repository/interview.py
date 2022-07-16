from typing import List

from fastapi import HTTPException
from jose import jwt, JWTError
from sqlalchemy import func
from sqlalchemy.orm import Session
from starlette import status

import api.models.interview as interview_model
import api.schemas.interview as interview_schema
import api.schemas.user as user_schema
from api.config.user import SECRET_KEY, ALGORITHM
import api.repository.user as user_repository


def create_interview(
        db: Session,
        interview_create: interview_schema.InterviewCreate,
        token: str,
) -> interview_model.Interview:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = user_schema.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = user_repository.get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception

    interview = interview_model.Interview(**interview_create.dict(), send_by=user.id)

    db.add(interview)
    db.commit()
    db.refresh(interview)

    return interview


def obtain_random_interviews(
        db: Session,
        token: str,
) -> List[interview_schema.Interview]:
    return db.query(interview_model.Interview) \
        .order_by(func.rand()) \
        .limit(5) \
        .all()


def bookmark_interviews(
        bookmark_request: interview_schema.BookmarkInterviewCreate,
        db: Session,
        token: str,
) -> List[interview_schema.Interview]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = user_schema.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = user_repository.get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception

    interview = db.query(interview_model.Interview)\
        .filter(interview_model.Interview.id == bookmark_request.interview_id).first()

    if not interview:
        not_found_exception = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find the interview",
        )
        raise not_found_exception

    bookmark = interview_model.Bookmark(**bookmark_request.dict(), user_id=user.id)

    db.add(bookmark)
    db.commit()
    db.refresh(bookmark)

    return bookmark

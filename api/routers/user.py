import datetime

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from api.config.user import ACCESS_TOKEN_EXPIRE_MINUTES
import api.schemas.user as user_schema
import api.repository.user as user_repository
from api.db import get_db

router = APIRouter()


@router.post('/signup', response_model=user_schema.UserInDB)
def signup(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    return user_repository.signup(db=db, username=form_data.username, password=form_data.password)


@router.post("/token", response_model=user_schema.Token)
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_repository.authenticate_user(db=db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = user_repository.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=user_schema.UserInDB)
def read_users_me(current_user: user_schema.UserInDB = Depends(user_repository.get_current_active_user)):
    return current_user

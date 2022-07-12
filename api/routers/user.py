import datetime

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from api.config.user import ACCESS_TOKEN_EXPIRE_MINUTES
import api.schemas.user as user_schema

router = APIRouter()


@router.post("/token", response_model=user_schema.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_schema.authenticate_user(user_schema.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = user_schema.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=user_schema.UserBase)
async def read_users_me(current_user: user_schema.UserBase = Depends(user_schema.get_current_active_user)):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(current_user: user_schema.UserBase = Depends(user_schema.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]

import datetime
from typing import Optional, Union

from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: Optional[str] = Field(None,
                                        example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c')
    token_type: Optional[str] = Field('bearer', example='bearer')


class TokenData(BaseModel):
    username: Union[str, None] = Field(None, example='test_user_name')


class UserBase(BaseModel):
    username: Optional[str] = Field(None, example='test_user_name')
    hashed_password: Optional[str] = Field(None, example='hogehoge')
    disabled: bool = Field(False, example=False)

    class Config:
        orm_mode = True


class UserInDB(UserBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True


class UserSignupRequest(BaseModel):
    username: Optional[str] = Field(None, example='test_user')
    plain_password: Optional[str] = Field(None, example='test_password')

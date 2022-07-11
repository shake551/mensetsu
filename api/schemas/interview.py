from typing import Optional

from pydantic import BaseModel, Field


class Interview(BaseModel):
    id: int
    content: Optional[str] = Field(None, example="これまで開発したもので一番自信があるものはなんですか")

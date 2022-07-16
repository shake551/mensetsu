from sqlalchemy import Boolean, Column, Integer, String, DATETIME
from sqlalchemy.schema import FetchedValue

from api.db import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    username = Column(String(1024))
    hashed_password = Column(String(1024))
    disabled = Column(Boolean, default=False)
    created_at = Column(DATETIME, FetchedValue())
    updated_at = Column(DATETIME, FetchedValue())

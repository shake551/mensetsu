from sqlalchemy import Boolean, Column, TIMESTAMP, Integer, String
from sqlalchemy.schema import FetchedValue

from api.db import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    username = Column(String(1024))
    password = Column(String(1024))
    disabled = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, FetchedValue())
    updated_at = Column(TIMESTAMP, FetchedValue())

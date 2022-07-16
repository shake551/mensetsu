from sqlalchemy import Column, TIMESTAMP, Integer, String, ForeignKey
from sqlalchemy.schema import FetchedValue

from api.db import Base
from api.models.user import User


class Interview(Base):
    __tablename__ = 'interviews'

    id = Column(Integer, primary_key=True)
    send_by = Column(Integer, ForeignKey('users.id'))
    content = Column(String(1024))
    created_at = Column(TIMESTAMP, FetchedValue())
    updated_at = Column(TIMESTAMP, FetchedValue())


class Bookmark(Base):
    __tablename__ = 'bookmarks'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    interview_id = Column(Integer, ForeignKey('interviews.id'), primary_key=True)
    created_at = Column(TIMESTAMP, FetchedValue())
    updated_at = Column(TIMESTAMP, FetchedValue())

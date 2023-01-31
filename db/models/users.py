from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .base import BaseModel


def now():
    return datetime.now()


class User(BaseModel):
    __tablename__ = 'users'

    chat_id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    language_code = Column(String)
    created_at = Column(DateTime(timezone=True), default=now)
    active = Column(Boolean, default=True)


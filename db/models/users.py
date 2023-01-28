from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime

from settings import metadata


def now():
    return datetime.now()


users = Table(
    'users', metadata,
    Column('chat_id',Integer, primary_key=True),
    Column('username', String, unique=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('language_code', String),
    Column('created_at', DateTime(timezone=True), default=now)
)

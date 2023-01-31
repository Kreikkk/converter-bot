from enum import Enum
from typing import Optional

from app.helpers import exception
from datetime import datetime
from pydantic import BaseModel, Field, root_validator, validator


class ServiceMessageStatuses(Enum):
    kicked = 'kicked'
    member = 'member'


class LanguageCodes(Enum):
    ru = 'ru'
    en = 'en'

    @classmethod
    def _missing_(cls, value):
        return cls.en


class ChatSerializer(BaseModel):
    chat_id: int = Field(alias='id')
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    language_code: str

    @validator('language_code')
    def validate_language_code(cls, code):
        try:
            return LanguageCodes(code).value
        except Exception:
            raise ValueError('Validation error')


class MessageSerializer(BaseModel):
    chat: ChatSerializer
    text: str
    date: datetime

    @root_validator(pre=True)
    @exception()
    def validate(cls, values):
        values['chat'] = values['from']
        values['date'] = datetime.fromtimestamp(values['date'])

        return values


class ServiceMessageSerializer(BaseModel):
    chat: ChatSerializer
    date: datetime
    status: ServiceMessageStatuses

    @root_validator(pre=True)
    @exception()
    def validate(cls, values):
        values['chat'] = values['from']
        values['status'] = values['new_chat_member']['status']

        return values
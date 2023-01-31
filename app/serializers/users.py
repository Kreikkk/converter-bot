from datetime import datetime
from pydantic import BaseModel


class UserSerializer(BaseModel):
    chat_id: int
    username: str
    first_name: str
    last_name: str
    language_code: str
    created_at: datetime
    active: bool


class SimpleUserSerializer(BaseModel):
    chat_id: int
    username: str

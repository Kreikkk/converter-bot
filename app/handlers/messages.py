from aiogram import types
from sqlalchemy import select

from app.serializers.messages import MessageSerializer
from db.connector import Connector
from db.models.users import User


async def echo(message: types.Message):
    ser = MessageSerializer(**dict(message))
    chat_id = ser.chat.chat_id

    async with Connector().connect() as conn:
        user = (await User.filter(conn, User.chat_id==chat_id)).fetchone()

    if not user:
        await message.answer(f'You are not registered yet, please restart the bot')
        return

    await message.answer(f'You wrote "{message.text}"!')

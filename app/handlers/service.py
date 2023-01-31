from aiogram import types
from sqlalchemy import select, insert, update

from app.serializers.messages import ServiceMessageSerializer, ServiceMessageStatuses
from db.connector import Connector
from db.models.users import User


async def handle_service(update_message: types.ChatMemberUpdated):
    ser = ServiceMessageSerializer(**dict(update_message))
    chat_id = ser.chat.chat_id

    async with Connector().connect() as conn:
        user = (await User.filter(conn, User.chat_id==chat_id)).fetchone()

        if not user:
            await User.create(conn, **ser.chat.dict(), active=ser.status==ServiceMessageStatuses.member)
        else:
            update_query = User.update_pre(User.chat_id==chat_id)

            if ser.status == ServiceMessageStatuses.member and not user.active:
                await conn.execute(update_query.values(active=True))
            elif ser.status == ServiceMessageStatuses.kicked and user.active:
                await conn.execute(update_query.values(active=False))

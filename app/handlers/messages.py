from random import choice
from aiogram import types

EMOJIS = '💓💖💗💞💕❤'


async def echo(message: types.Message):
    await message.answer(f'Ты написала "{message.text}"! {choice(list(EMOJIS))}')

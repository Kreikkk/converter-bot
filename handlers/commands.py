from aiogram import types


async def handle_start(message: types.Message):
    await message.reply("Привет! Всё работает!")

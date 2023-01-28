from aiogram import types


async def handle_start(message: types.Message):
    await message.reply("Hi! It works!")

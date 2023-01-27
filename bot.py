import logging

import handlers

from aiogram import executor, Bot, Dispatcher

from settings import BOT_TOKEN


logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot)


if __name__ == '__main__':
    dispatcher.register_message_handler(handlers.handle_start, commands=["start", "help"])
    dispatcher.register_message_handler(handlers.echo)

    executor.start_polling(dispatcher, skip_updates=True)
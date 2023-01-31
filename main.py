from app import handlers

from aiogram import executor, Bot, Dispatcher

from settings import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot)


if __name__ == '__main__':
    dispatcher.register_message_handler(handlers.handle_start, commands=['start',])
    dispatcher.register_message_handler(handlers.echo)
    dispatcher.register_my_chat_member_handler(handlers.handle_service)

    executor.start_polling(dispatcher)

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.config import load_config
from bot.handlers.user import register_user

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.INFO)
    config = load_config("bot.ini")

    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=storage)

    # Регистрация handlers
    register_user(dp)

    # start
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())

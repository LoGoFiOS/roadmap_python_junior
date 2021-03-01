import asyncio
import logging

import asyncpg
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot import config
from bot.handlers.user import register_user
from bot.middlewares.throttling import ThrottlingMiddleware
from bot.middlewares.db import DbMiddleware

logger = logging.getLogger(__name__)


# def create_pool(user, password, host, database):
#     raise NotImplementedError


async def main():
    logging.basicConfig(level=logging.INFO)

    storage = MemoryStorage()
    bot = Bot(token=config.TELEGRAM_API_TOKEN)
    dp = Dispatcher(bot, storage=storage)

    # Работа с БД
    pool = await asyncpg.create_pool(
        user=config.PG_USER,
        password=config.PG_PASSWORD,
        host=config.PG_HOST,
        database=config.PG_DATABASE,
    )

    await pool.execute(
            "CREATE TABLE IF NOT EXISTS users "
            "(id INT NOT NULL, name varchar(255) NOT NULL, email varchar(255), PRIMARY KEY (id));"
        )

    dp.middleware.setup(DbMiddleware(pool))

    dp.middleware.setup(ThrottlingMiddleware())
    register_user(dp)

    try:
        await dp.start_polling()
    finally:
        await bot.close()

if __name__ == '__main__':
    asyncio.run(main())



    # Работа с SQlite
    # import bot.db_docker.sqlite as database
    # db_docker = database.set_config(path_to_db='bot/db_docker/mysqlite.db_docker')

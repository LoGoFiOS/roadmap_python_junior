from random import randint
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from bot.utils.ref_generator import get_ref
from bot.db.repository import Repo


async def my_ref(m: types.Message):
    await m.answer(get_ref(m.from_user.id))


async def bot_echo(m: types.Message):
    await m.reply("hi")


async def bot_start(message: types.Message, repo: Repo):
    name = message.from_user.full_name
    await repo.add_user(user_id=message.from_user.id, user_name=name)
    await message.answer(
        "\n".join(
            [
                f'Привет, {message.from_user.full_name}!',
                f'Ты был занесен в базу'
            ]))


async def add_user(m: types.Message, repo: Repo):
    await repo.add_user(user_id=randint(1, 9000), user_name="XZ", user_email="gm")


async def show_db(m: types.Message, repo: Repo):
    await m.answer(await repo.show_db())
    await m.answer(await repo.select_user(id=23466746))


def register_user(dp: Dispatcher):
    dp.register_message_handler(my_ref, commands=["ref"])
    dp.register_message_handler(show_db, commands=["show"])
    dp.register_message_handler(add_user, commands=["add"])
    dp.register_message_handler(bot_start, CommandStart)
    dp.register_message_handler(bot_echo)


# sqlite
# async def add_user(m: types.Message):
#     name = m.from_user.username
#     id = m.from_user.id
#     try:
#         database.add_user(id=id, name=name)
#     except sqlite3.IntegrityError as e:
#         print(e)

# пример использования антифлуда
# @rate_limit(limit=2)
# async def bot_echo(m: types.Message):
#     await m.answer("hello")
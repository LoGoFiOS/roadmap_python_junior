import re

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters.builtin import Text


class GetInformation(StatesGroup):
    waiting_name = State()
    waiting_email = State()
    waiting_phone_num = State()


async def user_start(msg: types.Message):
    await msg.answer(f"Начинаю регистрацию.\n"
                     f"Для начала, как тебя зовут?")
    await GetInformation.waiting_name.set()


async def get_name(msg: types.Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await GetInformation.next()
    await msg.answer("Теперь введи свой email:")


async def get_email(msg: types.Message, state: FSMContext):
    regexp_result = re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", msg.text)
    if not regexp_result:
        await msg.answer("Введите корректный email!")
        return
    await state.update_data(email=msg.text)
    await GetInformation.next()
    await msg.answer("Теперь введи свой номер телефона:")


async def get_phone_num(msg: types.Message, state: FSMContext):
    await state.update_data(phone_num=msg.text)
    user_data = await state.get_data()
    await msg.answer(f"Привет! Ты ввел следующие данные:\n"
                     f"Имя - {user_data['name']}\n"
                     f"Email - {user_data['email']}\n"
                     f"Телефон: - {user_data['phone_num']}\n")
    await state.finish()


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["form"], state="*")
    dp.register_message_handler(get_name, state=GetInformation.waiting_name)
    dp.register_message_handler(get_email, state=GetInformation.waiting_email)
    dp.register_message_handler(get_phone_num, state=GetInformation.waiting_phone_num)

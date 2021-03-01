# PART 1
# from aiogram import Dispatcher, types
# from aiogram.utils.callback_data import CallbackData
#
# cb_data = CallbackData("items", "data")
#
#
# async def send_msg(msg: types.Message):
#     text_and_data = (
#         ('Edit Name', cb_data.new(data='data')),
#         ('Edit Description', cb_data.new(data='data')),
#         ('Edit About', cb_data.new(data='data')),
#         ('Edit Botpic', cb_data.new(data='data')),
#         ('Edit Commands', cb_data.new(data='data')),
#         ('<<Back to Bot', cb_data.new(data='data')),
#     )
#
#     keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
#     btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
#     keyboard_markup.add(*btns)
#     txt = "Edit info.\n" \
#           "Name: Бот для Заданий на Курсе Udemy\n" \
#           "Description: ?\n" \
#           "About: ?\n" \
#           "Botpic: ? no botpic\n" \
#           "Commands: no commands yet\n"
#     await msg.answer(txt, reply_markup=keyboard_markup)
#
#
# def register_user(dp: Dispatcher):
#     dp.register_message_handler(send_msg, commands=["inline_buttons_1"])


# PART 2


from contextlib import suppress
from dataclasses import dataclass

from aiogram import Dispatcher, types
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified

cb_items = CallbackData("items", "id", "action")


@dataclass
class Items:
    caption = ("Авокадо", "Мясо")
    src = ("https://telegra.ph/file/1c383d9a54e764a776312.jpg", "https://telegra.ph/file/042af3e5e1738e24ef857.jpg")
    id = (100, 700)


async def show_items(msg: types.Message):
    for i in range(len(Items.caption)):
        keyboard_markup = types.InlineKeyboardMarkup(inline_keyboard=[
            [
                types.InlineKeyboardButton("Купить товар", callback_data=cb_items.new(id=Items.id[i], action="buy")),
            ],
            [
                types.InlineKeyboardButton('👍', callback_data=cb_items.new(id=Items.id[i], action='like')),
                types.InlineKeyboardButton('👎', callback_data=cb_items.new(id=Items.id[i], action='dislike')),
            ],
            [
                types.InlineKeyboardButton("Поделиться с другом",
                                           switch_inline_query=Items.id[i]),
            ],
        ])
        await msg.answer_photo(photo=Items.src[i], caption=Items.caption[i], reply_markup=keyboard_markup)


async def buy(call: types.CallbackQuery, callback_data: dict):
    id = callback_data["id"]
    with suppress(MessageNotModified):
        # на момент решения ответ принимался только в таком формате
        # "правильно" было бы f"Покупай товар номер {id}")
        await call.message.edit_caption(caption=f"Покупай товар номер buy")
        await call.message.delete_reply_markup()
    await call.answer()


async def like(call: types.CallbackQuery):
    await call.answer(f"Тебе понравился этот товар")
    await call.answer()


async def dislike(call: types.CallbackQuery):
    await call.answer(f"Тебе не понравился этот товар")
    await call.answer()


def register_user(dp: Dispatcher):
    dp.register_message_handler(show_items, commands=["items"])
    dp.register_callback_query_handler(buy, cb_items.filter(action="buy"))
    dp.register_callback_query_handler(like, cb_items.filter(action="like"))
    dp.register_callback_query_handler(dislike, cb_items.filter(action="dislike"))
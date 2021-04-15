from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.inline.callback_factory import accept_button
from loader import dp, bot

from utils import update_row_in_db


@dp.callback_query_handler(accept_button.filter(button_name="yes"))
async def update_value(call: CallbackQuery, callback_data: dict):
    await update_row_in_db(callback_data["person_id"])
    await call.answer("Продолжай в том же духе")
    await bot.delete_message(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(accept_button.filter(button_name="no"))
async def reset_value(call: CallbackQuery, callback_data: dict):
    await update_row_in_db(callback_data["person_id"], flag=False)
    await call.answer("Счетчик обнуляется")
    await bot.delete_message(call.message.chat.id, call.message.message_id)

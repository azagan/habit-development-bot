from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram.types import Message
from keyboards.default import menu
from aiogram.dispatcher.filters import Command, Text
from states import AddEvent

from utils import (select_row_in_db,
                   update_row_in_db,
                   insert_row_to_db)

from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Выбери действие", reply_markup=menu)


@dp.message_handler(Text(equals="Добавить событие"))
async def add_event(message: Message):
    await message.answer("Какое событие хочешь добавить?")
    await AddEvent.event_mess.set()


@dp.message_handler(state=AddEvent.event_mess)
async def get_event(message: Message, state: FSMContext):
    text = message.text
    # async with state.proxy() as data:
    #     data["event"] = text
    await insert_row_to_db(text)
    await message.answer(f"Событие '{text}' добавлено в список")
    await state.reset_state()


@dp.message_handler(Text(equals="Посмотреть все события"))
async def get_all_events(message: Message):
    event_success_id = await select_row_in_db()
    text = ""
    for ev, suc, ids in event_success_id:
        text += f"{ev} - выполняется: {suc}\n"
    await message.answer(text)

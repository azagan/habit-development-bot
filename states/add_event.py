from aiogram.dispatcher.filters.state import StatesGroup, State


class AddEvent(StatesGroup):
    event_mess = State()

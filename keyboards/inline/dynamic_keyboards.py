from aiogram.types import InlineKeyboardMarkup

from keyboards.inline.callback_factory import accept_button


def get_dynamic_keyboard(ids: int) -> InlineKeyboardMarkup:
    menu = InlineKeyboardMarkup()
    menu.add(
        InlineKeyboardMarkup(
            text="Да",
            callback_data=accept_button.new(
                button_name="yes",
                person_id=ids
            )
        )
    )
    menu.add(
        InlineKeyboardMarkup(
            text="Нет",
            callback_data=accept_button.new(
                button_name="no",
                person_id=ids
            )
        )
    )
    return menu

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить событие"),
        ],
        [
            KeyboardButton(text="Посмотреть все события")
        ],
    ],
    resize_keyboard=True
)

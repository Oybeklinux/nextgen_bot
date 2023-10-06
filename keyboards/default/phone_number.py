from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Отправить номер", request_contact=True)],

    ], resize_keyboard=True
)

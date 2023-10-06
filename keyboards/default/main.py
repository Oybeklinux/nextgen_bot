from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔍 Курсы"),KeyboardButton(text="⚙ Настройки")],
    ], resize_keyboard=True
)

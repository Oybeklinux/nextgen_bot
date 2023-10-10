from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.texts import Texts

def get_main_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=Texts.get("bcourses")),KeyboardButton(text=Texts.get("bsettings"))],
        ], resize_keyboard=True
    )

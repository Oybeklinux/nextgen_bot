from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.texts import Texts


def get_settings_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=Texts().get("bedit_lang")), KeyboardButton(text=Texts().get("bedit_name"))],
            [KeyboardButton(text=Texts().get("bsend_phone")), KeyboardButton(text=Texts().get("bto_main"))],
        ], resize_keyboard=True
    )

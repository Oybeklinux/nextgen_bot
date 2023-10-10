from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.texts import Texts


def get_phone_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=Texts.get('bsend_phone'), request_contact=True)],

        ], resize_keyboard=True
    )

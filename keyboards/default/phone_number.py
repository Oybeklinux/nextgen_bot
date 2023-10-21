from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.texts import _


async def get_phone_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=await _('bsend_phone'), request_contact=True)],

        ], resize_keyboard=True
    )

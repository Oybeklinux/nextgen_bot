from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.texts import _


async def get_main_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=await _("bcourses")),KeyboardButton(text=await _("bsettings"))],
        ], resize_keyboard=True
    )

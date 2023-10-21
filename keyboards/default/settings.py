from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.texts import _


async def get_settings_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=await _("bedit_lang")), KeyboardButton(text=await _("bto_main"))],
            # [KeyboardButton(text=Texts().get("bsend_phone")), KeyboardButton(text=Texts().get("bedit_name"))],
        ], resize_keyboard=True
    )

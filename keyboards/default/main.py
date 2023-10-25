from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, User

from data.config import admins
from data.texts import _
from loader import db


async def get_main_kb():

    if User.get_current().id not in admins:
        keyboars = [
            [KeyboardButton(text=await _("bсontest")), KeyboardButton(text=await _("bсontest_users"))],
            [KeyboardButton(text=await _("bcourses")), KeyboardButton(text=await _("bsettings"))],
        ]

    else:
        keyboars = [
            [KeyboardButton(text=await _("bсontest")),KeyboardButton(text=await _("bstart")), KeyboardButton(text=await _('bstop'))],
            [KeyboardButton(text=await _('random_choice')), KeyboardButton(text=await _("bсontest_users"))],
            [KeyboardButton(text=await _("bcourses")), KeyboardButton(text=await _("bsettings"))],
        ]

    return ReplyKeyboardMarkup(
        keyboard=keyboars, resize_keyboard=True
    )

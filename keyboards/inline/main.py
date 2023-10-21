from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from data.texts import _

maincb = CallbackData("menu", 'submenu')


async def get_main_ikb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=await _('bcourses'), switch_inline_query_current_chat='')],
            # [InlineKeyboardButton(text="IT-тест 🧠", callback_data=maincb.new(submenu='it_test'))],
            [InlineKeyboardButton(text=await _("iabout_us"), callback_data=maincb.new(submenu='about')),
             InlineKeyboardButton(text=await _("icontact"), callback_data=maincb.new(submenu='contacts'))],
            [InlineKeyboardButton(text=await _("iopen_lesson"), callback_data=maincb.new(submenu='open_lessons')),
             InlineKeyboardButton(text=await _("iwebsite"), url='https://ngen.uz/')]
        ]
    )

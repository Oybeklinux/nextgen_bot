from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from data.texts import Texts

maincb = CallbackData("menu", 'submenu')


def get_main_ikb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=Texts.get('bcourses'), switch_inline_query_current_chat='')],
            # [InlineKeyboardButton(text="IT-тест 🧠", callback_data=maincb.new(submenu='it_test'))],
            [InlineKeyboardButton(text=Texts().get("iabout_us"), callback_data=maincb.new(submenu='about')),
             InlineKeyboardButton(text=Texts().get("icantact"), callback_data=maincb.new(submenu='contacts'))],
            # [InlineKeyboardButton(text="Открытые уроки 📌", callback_data=maincb.new(submenu='open_lessons')),
            #  InlineKeyboardButton(text="Посетить сайть 🌐", callback_data=maincb.new(submenu='web_site'))]
        ]
    )

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from keyboards import general_cb
from loader import db

open_lessons_cb = CallbackData('open_lesson_types_menu', "course")


async def get_open_lessons():
    rows = await db.select_courses(only_desc=True)
    inline_keyboard = []
    for row in rows:
        inline_keyboard.append(
            [InlineKeyboardButton(text=row['official_name'], callback_data=general_cb.new(submenu='register_to_open_lesson_vip', course=row['name'], is_menu=True))])

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

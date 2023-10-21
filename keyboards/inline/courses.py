from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from data.texts import _

# register to open lesson
general_cb = CallbackData("course_menu", 'course', 'submenu', 'is_menu')


async def get_general_ikb(course):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                # InlineKeyboardButton(text=Texts().get("iopen_lesson"),
                #                   callback_data=register_ol_cb.new(course=course, submenu='register_to_open_lesson')),
            InlineKeyboardButton(text=await _("iopen_lesson_vip"),
                                 callback_data=general_cb.new(course=course, submenu='register_to_open_lesson_vip', is_menu=None)),
             InlineKeyboardButton(text=await _("iget_in_touch"),
                                  url='https://t.me/kamilaa3')],
            [InlineKeyboardButton(text=await _("icourse_content"),
                                  callback_data=general_cb.new(submenu="course_content", course=course, is_menu=None)),
             InlineKeyboardButton(text=await _("icourse_objective"),
                                  callback_data=general_cb.new(submenu="course_objective", course=course, is_menu=None))],
            [InlineKeyboardButton(text=await _("bto_main"),
                                  callback_data=back_to_course_cb.new(value='back'))]
        ]
    )


confirm_ol_cb = CallbackData("confirm_ol", 'submenu')


async def get_confirm_ol_ikb(course):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=await _("iconfirm"),callback_data=confirm_ol_cb.new(submenu=course)),
            InlineKeyboardButton(text=await _("icancel"), callback_data=confirm_ol_cb.new(submenu='cancel'))
            ]
        ]
    )


back_to_course_cb = CallbackData("back_to_course", 'value')


async def get_back_to_course_ikb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=await _("bto_main"), callback_data=back_to_course_cb.new(value='back'))],
        ]
    )

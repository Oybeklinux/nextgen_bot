from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from data.texts import Texts

# register to open lesson
register_ol_cb = CallbackData("course_menu",'course', 'submenu', 'lesson_id')


def get_course_ikb(course):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                # InlineKeyboardButton(text=Texts().get("iopen_lesson"),
                #                   callback_data=register_ol_cb.new(course=course, submenu='register_to_open_lesson')),
            InlineKeyboardButton(text=Texts().get("iopen_lesson_vip"),
                                     callback_data=register_ol_cb.new(course=course, submenu='register_to_open_lesson_vip')),
             InlineKeyboardButton(text=Texts().get("iget_in_touch"),
                                  url='https://t.me/kamilaa3')],
            [InlineKeyboardButton(text=Texts().get("icourse_content"),
                                  callback_data=register_ol_cb.new(submenu="course_content", course=course)),
             InlineKeyboardButton(text=Texts().get("icourse_objective"),
                                  callback_data=register_ol_cb.new(submenu="course_objective", course=course))],
            [InlineKeyboardButton(text=Texts().get("bto_main"),
                                  callback_data=back_to_course_cb.new(value='back'))]
        ]
    )


confirm_ol_cb = CallbackData("confirm_ol", 'submenu')


def get_confirm_ol_ikb(course):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=Texts.get("iconfirm"),callback_data=confirm_ol_cb.new(submenu=course)),
            InlineKeyboardButton(text=Texts.get("icancel"), callback_data=confirm_ol_cb.new(submenu='cancel'))
            ]
        ]
    )


back_to_course_cb = CallbackData("back_to_course", 'value')

def get_back_to_course_ikb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=Texts.get("bto_main"), callback_data=back_to_course_cb.new(value='back'))],
        ]
    )

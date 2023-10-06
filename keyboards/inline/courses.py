from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

# register to open lesson
register_ol_cb = CallbackData("course", 'submenu')


def get_course_ikb(course):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открытый урок", callback_data=register_ol_cb.new(submenu=course)),
             InlineKeyboardButton(text="Связаться", url='https://t.me/kamilaa3')],
            [InlineKeyboardButton(text="⬅ Назад", callback_data=back_to_course_cb.new(value='back'))]
        ]
    )


confirm_ol_cb = CallbackData("confirm_ol", 'submenu')


def get_confirm_ol_ikb(course):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Подтвердить ✅",callback_data=confirm_ol_cb.new(submenu=course)),
            InlineKeyboardButton(text="Отмена ❌",callback_data=confirm_ol_cb.new(submenu='cancel'))
            ]
        ]
    )


back_to_course_cb = CallbackData("back_to_course", 'value')

back_to_course_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅ Назад", callback_data=back_to_course_cb.new(value='back'))],
    ]
)

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


maincb = CallbackData("menu", 'submenu')

main_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Курсы 💻", switch_inline_query_current_chat='')],
        # [InlineKeyboardButton(text="IT-тест 🧠", callback_data=maincb.new(submenu='it_test'))],
        [InlineKeyboardButton(text="О нас ❓", callback_data=maincb.new(submenu='about')),
         InlineKeyboardButton(text="Контакты 📱", callback_data=maincb.new(submenu='contacts'))],
        # [InlineKeyboardButton(text="Открытые уроки 📌", callback_data=maincb.new(submenu='open_lessons')),
        #  InlineKeyboardButton(text="Посетить сайть 🌐", callback_data=maincb.new(submenu='web_site'))]
    ]
)

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


language_cb = CallbackData("language_menu", 'language')

language_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data=language_cb.new(language='uz'))],
        [InlineKeyboardButton(text="🇷🇺 Русский язык", callback_data=language_cb.new(language='ru'))],
        [InlineKeyboardButton(text="🇬🇧 English", callback_data=language_cb.new(language='en'))],
    ]
)

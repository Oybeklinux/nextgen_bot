from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.callback_data import CallbackData

from data.config import main_text
from keyboards.inline.main_ikb import *
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')
    await send_main_menu(message)


async def send_main_menu(message: types.Message) -> None:
    text = main_text.replace("#full_name", message.from_user.full_name)
    await message.answer(text, reply_markup=main_ikb)

# Главное -> IT-тест 🧠
@dp.callback_query_handler(maincb.filter(submenu='it_test'))
async def it_test(callback: types.CallbackQuery):
    await callback.message.answer("Вы вибрали IT-тест 🧠")

# Главное -> О нас ❓"
@dp.callback_query_handler(maincb.filter(submenu='about'))
async def about_us(callback: types.CallbackQuery):
    await callback.message.answer("Вы вибрали О нас ❓")

# Главное -> Контакты 📱"
@dp.callback_query_handler(maincb.filter(submenu='contacts'))
async def courses(callback: types.CallbackQuery):
    await callback.message.answer("Вы вибрали Контакты 📱")

# Главное -> Открытые уроки 📌"
@dp.callback_query_handler(maincb.filter(submenu='open_lessons'))
async def open_lessons(callback: types.CallbackQuery):
    await callback.message.answer("Вы вибрали Открытые уроки 📌")

# Главное -> Посетить сайть 🌐"
@dp.callback_query_handler(maincb.filter(submenu='web_site'))
async def web_site(callback: types.CallbackQuery):
    await callback.message.answer("Вы вибрали Посетить сайть 🌐")

# Главное -> Курсы 💻 -> Поиск
@dp.inline_handler(text='')
async def search(query: types.InlineQuery):
    search_word = query.query or ''
    print('$$$',search_word)
    results = [types.InlineQueryResultArticle(
        id='1',
        # photo_file_id='AgACAgIAAxkDAAIDPGUahKut1oTCPQ9mkeP-IUSpCjqRAAJe0DEb_lXQSKLHas9TVdRtAQADAgADcwADMAQ',
        title='Python и Django',
        description='Создание сайтов и веб-приложений',
        input_message_content=types.InputTextMessageContent(
            message_text='Python'
        )
    ),
        types.InlineQueryResultArticle(
            id='2',
            # photo_file_id='AgACAgIAAxkDAAIDTmUah__sf_YaE_ibWPvordCc2qmIAAJY0DEb_lXQSGSbh-VqEi8DAQADAgADcwADMAQ',
            title='Flutter. Dart',
            description='Разработка приложений под различные операционные системы',
            input_message_content=types.InputTextMessageContent(
                message_text='Flutter'
            )
        )
    ]
    # oybek AgACAgIAAxkDAAIDPGUahKut1oTCPQ9mkeP-IUSpCjqRAAJe0DEb_lXQSKLHas9TVdRtAQADAgADcwADMAQ
    # hurshid aka AgACAgIAAxkDAAIDTmUah__sf_YaE_ibWPvordCc2qmIAAJY0DEb_lXQSGSbh-VqEi8DAQADAgADcwADMAQ

    await query.answer(results,cache_time=1,is_personal=True)
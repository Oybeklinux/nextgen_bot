from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import filters
from aiogram.types import ParseMode

from data.config import admins
from data.texts import open_lesson_dates as ol_dates
from filters.is_in import IsIn
from keyboards import *
from datetime import datetime
from loader import dp


@dp.message_handler(filters.Regexp(r'course_.+#'))
async def courses_selected(message: types.Message):

    selected_course = message.text.replace('#', '').replace('course_', '').lower()
    await message.delete()
    if selected_course == 'php':
        text = Texts.get('php')
        thumb_url='https://telegra.ph/file/62bb42714b939611154db.png'
    elif selected_course == 'python':
        thumb_url = 'https://telegra.ph/file/1ed2732d276af0a239ca1.png'
        text = Texts.get("python")
    elif selected_course == 'flutter':
        thumb_url = 'https://telegra.ph/file/7aa34eeab125b70322d44.png'
        text = Texts.get('flutter')

    text = f"<a href='{thumb_url}'> </a>{text}"

    await message.answer(text=text,
                         reply_markup=get_course_ikb(selected_course),
                         parse_mode=ParseMode.HTML)


# Назад к курсу
@dp.callback_query_handler(back_to_course_cb.filter())
async def back_to_course(callback: types.CallbackQuery) -> None:
    await callback.message.delete()


# Курсы
@dp.message_handler(IsIn("bcourses"))
@dp.message_handler(Command('courses'))
async def send_main_menu(message: types.Message) -> None:
    await message.answer(Texts.get("courses"), reply_markup=get_main_ikb(), parse_mode=ParseMode.MARKDOWN)


# Главное -> IT-тест 🧠
@dp.callback_query_handler(maincb.filter(submenu='it_test'))
async def it_test(callback: types.CallbackQuery):
    await callback.message.answer("Вы вибрали IT-тест 🧠")


# Главное -> О нас ❓"
@dp.callback_query_handler(maincb.filter(submenu='about'))
async def about_us(callback: types.CallbackQuery):
    about_url = 'https://telegra.ph/file/0f8ae82aa7617e7164431.png'
    await callback.message.answer_video(
        video='https://telegra.ph//file/b58dd2c66ab9cbce1ffa7.mp4',
        caption=Texts.get('about_us'),
        parse_mode=ParseMode.HTML,
        reply_markup=back_to_course_ikb)


# Главное -> Контакты 📱"
@dp.callback_query_handler(maincb.filter(submenu='contacts'))
async def contacts(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo='https://telegra.ph/file/0f8ae82aa7617e7164431.png',
        caption=Texts.get("contact"),
        parse_mode=ParseMode.MARKDOWN, reply_markup=back_to_course_ikb)


# # Главное -> Открытые уроки 📌"
# @dp.callback_query_handler(maincb.filter(submenu='open_lessons'))
# async def open_lessons(callback: types.CallbackQuery):
#
#     await callback.message.answer(f"Вы вибрали Открытые уроки по 📌")


# # Главное -> Посетить сайть 🌐"
# @dp.callback_query_handler(maincb.filter(submenu='web_site'))
# async def web_site(callback: types.CallbackQuery):
#     await callback.message.answer("Вы вибрали Посетить сайть 🌐")


# Главное -> Курсы -> Записаться на открытий урок -> "
@dp.callback_query_handler(register_ol_cb.filter())
async def confirm_to_open_lesson(callback: types.CallbackQuery):
    course = register_ol_cb.parse(callback.data)['submenu']
    dt = ol_dates[course]['date']
    tm = ol_dates[course]['time']

    text = Texts.get("open_lesson")
    if course in ol_dates:
        text = text.replace('#course', course).replace('#date',dt).replace('#time', tm)
        await callback.message.answer(text, reply_markup=get_confirm_ol_ikb(course))


# Главное -> Курсы -> Записаться на открытий урок -> "
@dp.callback_query_handler(confirm_ol_cb.filter(submenu='cancel'))
async def confirm_to_open_lesson(callback: types.CallbackQuery):
    await callback.message.delete()


# Главное -> Курсы -> Записаться на открытий урок -> "
@dp.callback_query_handler(confirm_ol_cb.filter())
async def confirm_to_open_lesson(callback: types.CallbackQuery):
    course = confirm_ol_cb.parse(callback.data)['submenu']
    text = f"""
    Клиент: {callback.message.from_user.mention}
    Записался на открытый урок по {course.title()}
    Дата записи: {datetime.now().strftime("%d-%m-%y %H:%M")}"""

    for manager in admins:
        await callback.bot.send_message(chat_id=manager,text=text)

    await callback.message.answer(text=Texts.get("open_lesson_confirm"))
    await callback.message.delete()



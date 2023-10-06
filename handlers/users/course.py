from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import filters
from aiogram.types import ParseMode
from data import *
from data.config import managers
from keyboards import *
from datetime import datetime
from loader import dp


@dp.message_handler(filters.Regexp(r'course_.+#'))
async def courses_selected(message: types.Message):

    selected_course = message.text.replace('#', '').replace('course_', '').lower()
    await message.delete()
    if selected_course == 'php':
        text = php_course_text
        thumb_url='https://telegra.ph/file/62bb42714b939611154db.png'
    elif selected_course == 'python':
        thumb_url = 'https://telegra.ph/file/1ed2732d276af0a239ca1.png'
        text = python_course_text
    elif selected_course == 'flutter':
        thumb_url = 'https://telegra.ph/file/7aa34eeab125b70322d44.png'
        text = flutter_course_text

    text = f"<a href='{thumb_url}'> </a>{text}"

    await message.answer(text=text,
                         reply_markup=get_course_ikb(selected_course),
                         parse_mode=ParseMode.HTML)


# Назад к курсу
@dp.callback_query_handler(back_to_course_cb.filter())
async def back_to_course(callback: types.CallbackQuery) -> None:

    # text = main_text.replace("#full_name", callback.message.from_user.full_name)
    # await callback.message.answer(text, parse_mode=ParseMode.MARKDOWN,reply_markup=main_ikb)
    await callback.message.delete()


# Курсы
@dp.message_handler(Command('courses'))
async def send_main_menu(message: types.Message) -> None:
    await message.answer(about_courses_text, reply_markup=main_ikb, parse_mode=ParseMode.MARKDOWN)


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
        caption=about_nextgen_text,
        parse_mode=ParseMode.HTML,
        reply_markup=back_to_course_ikb)


# Главное -> Контакты 📱"
@dp.callback_query_handler(maincb.filter(submenu='contacts'))
async def contacts(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo='https://telegra.ph/file/0f8ae82aa7617e7164431.png',
        caption=contact_text,
        parse_mode=ParseMode.MARKDOWN, reply_markup=back_to_course_ikb)


# Главное -> Открытые уроки 📌"
@dp.callback_query_handler(maincb.filter(submenu='open_lessons'))
async def open_lessons(callback: types.CallbackQuery):
    await callback.message.answer(f"Вы вибрали Открытые уроки по 📌")


# Главное -> Посетить сайть 🌐"
@dp.callback_query_handler(maincb.filter(submenu='web_site'))
async def web_site(callback: types.CallbackQuery):
    await callback.message.answer("Вы вибрали Посетить сайть 🌐")


# Главное -> Курсы -> Записаться на открытий урок -> "
@dp.callback_query_handler(register_ol_cb.filter())
async def confirm_to_open_lesson(callback: types.CallbackQuery):
    course = register_ol_cb.parse(callback.data)['submenu']

    if course == 'python':
        text = confirm_ol_python_text
    elif course == 'php':
        text = confirm_ol_php_text
    elif course == 'flutter':
        text = confirm_ol_flutter_text
    else:
        return

    await callback.message.answer(text, reply_markup=get_confirm_ol_ikb(course))


# Главное -> Курсы -> Записаться на открытий урок -> "
@dp.callback_query_handler(confirm_ol_cb.filter(submenu='cancel'))
async def confirm_to_open_lesson(callback: types.CallbackQuery):
    await callback.message.delete()


# Главное -> Курсы -> Записаться на открытий урок -> "
@dp.callback_query_handler(confirm_ol_cb.filter())
async def confirm_to_open_lesson(callback: types.CallbackQuery):
    course = confirm_ol_cb.parse(callback.data)['submenu']
    user_id = callback.message.from_user.id
    text = f"""
    Клиент: {callback.message.from_user.mention}
    Записался на открытый урок по {course.title()}
    Дата: {datetime.now().strftime("%d-%m-%y %H:%M")}"""

    # for manager in managers:
    #     await callback.bot.send_message(chat_id=manager,text=text)

    await callback.message.answer(text=after_register_text)
    await callback.message.delete()



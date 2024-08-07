from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import filters
from aiogram.types import ParseMode
from data.config import admins
from data.texts import _
from filters.is_in import IsIn
from keyboards import *
from datetime import datetime

from keyboards.inline.open_lessons import get_open_lessons, open_lessons_cb
from loader import dp, db


@dp.message_handler(filters.Regexp(r'course_.+#'))
async def courses_selected(message: types.Message):
    selected_course = message.text.replace('#', '').replace('course_', '').lower()
    user_id = message.from_user.id
    print(f"user_id: {user_id}, selected_course: {selected_course}")
    row = await db.select_course_by_name(user_id, name=selected_course)
    text = await _('course')
    text = text.\
        replace('#about', f'{row[3]}\n\n').\
        replace('#career', f'{row[4]}\n\n').\
        replace('#for_whom', f'{row[5]}\n\n').\
        replace('#requirements', f'{row[6]}\n\n').\
        replace('#course_name', row[8])
    text = f"<a href='{row[7]}'> </a>{text}"

    await message.delete()

    await message.answer(text=text,
                         reply_markup=await get_general_ikb(selected_course),
                         parse_mode=ParseMode.HTML)


# click back button
@dp.callback_query_handler(back_to_course_cb.filter())
async def back_to_course(callback: types.CallbackQuery) -> None:
    await callback.message.delete()


# /courses
@dp.message_handler(IsIn("bcourses"))
@dp.message_handler(Command('courses'))
async def send_main_menu(message: types.Message) -> None:
    rows = await db.select_courses(only_desc=True)
    text = ''
    for row in rows:
        text += f"🔹 *{row[2]}*. {row[1]}\n"
    text = text.strip()
    text = (await _("courses")).replace("#courses", text)

    await message.answer(text, reply_markup=await get_main_ikb(), parse_mode=ParseMode.MARKDOWN)


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
        caption=await _('about_us'),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await get_back_to_course_ikb())
    await callback.answer()


# Главное -> Контакты 📱"
@dp.callback_query_handler(maincb.filter(submenu='contacts'))
async def contacts(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo='https://telegra.ph/file/0f8ae82aa7617e7164431.png',
        caption=await _("contact"),
        parse_mode=ParseMode.MARKDOWN, reply_markup=await get_back_to_course_ikb())
    await callback.answer()

# Главное -> Открытые уроки 📌"
@dp.callback_query_handler(maincb.filter(submenu='open_lessons'))
async def open_lessons(callback: types.CallbackQuery):
    await callback.message.answer(text="Sizni qaysi kurs bo'yicha ochiq dars qiziqtiradi?",
                                  reply_markup=await get_open_lessons())


# Главное -> Посетить сайть 🌐"
@dp.callback_query_handler(maincb.filter(submenu='web_site'))
async def web_site(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали Посетить сайть 🌐")


@dp.callback_query_handler(general_cb.filter(submenu="course_content"))
async def course_curriculum(callback: types.CallbackQuery) -> None:
    course = general_cb.parse(callback.data)['course']
    user_id = callback.from_user.id

    text = await db.select_course_curriculum(user_id, course)
    if text:
        await callback.message.answer(f"*{await _('icourse_content')}*\n\n{text[0]}",
                                  reply_markup=await get_back_to_course_ikb(),
                                  parse_mode=ParseMode.MARKDOWN)


@dp.callback_query_handler(general_cb.filter(submenu="course_objective"))
async def course_objective(callback: types.CallbackQuery) -> None:
    user_id = callback.from_user.id
    course = general_cb.parse(callback.data)['course']
    text = await db.select_course_objective(user_id, course)
    if text:
        await callback.message.answer(f"*{await _('icourse_objective')}*\n\n{text[0]}",
                                  reply_markup=await get_back_to_course_ikb(),
                                  parse_mode=ParseMode.MARKDOWN)


@dp.callback_query_handler(general_cb.filter(submenu='register_to_open_lesson_vip'))
async def confirm_to_open_lesson(callback: types.CallbackQuery):
    data = general_cb.parse(callback.data)
    course = data['course']
    if data['is_menu']:
        await callback.message.delete()
    await callback.answer()
    user = await db.select_user(id=callback.from_user.id)
    text = f"""
    Клиент: {callback.from_user.mention} 
    Записался на открытый урок по *{course.title()}*
    Телефон клиента: {user[4]}
    Имя клиента: {user[1]}
    Дата записи: {datetime.now().strftime("%d.%m.%Y %H:%M")}"""
    await db.insert_open_lesson_users(user_id=callback.from_user.id, course_name=course)
    for manager in admins:
        await callback.bot.send_message(chat_id=manager, text=text, parse_mode=ParseMode.MARKDOWN)

    await callback.message.answer(text=await _("open_lesson_confirm"))


# registering to open class
@dp.callback_query_handler(general_cb.filter(submenu='register_to_open_lesson'))
async def confirm_to_open_lesson(callback: types.CallbackQuery):
    data = general_cb.parse(callback.data)
    course = data['course']

    row = await db.select_open_lesson(course=course)

    datetime_str = f'{row[0]} {row[1]}'
    datetime_object = datetime.strptime(datetime_str, '%d.%m.%Y %H:%M')

    if datetime_object < datetime.now():
        text = await _('excuse_open_lesson').\
            replace('#date', row[0]).\
            replace('#time', row[1]).\
            replace('#course', row[3])

        await callback.message.answer(text,
                                      parse_mode=ParseMode.MARKDOWN)
        return

    text = await _('open_lesson').\
        replace('#course', course.title()).\
        replace('#date', row[0]).\
        replace('#time', row[1]).\
        replace('#button', await _('iconfirm')).\
        replace('#language', await _(row[2]))

    if row:
        await callback.message.answer(text,
                                      reply_markup=get_confirm_ol_ikb(course),
                                      parse_mode=ParseMode.MARKDOWN)

# Cancel registering to open class
@dp.callback_query_handler(confirm_ol_cb.filter(submenu='cancel'))
async def confirm_to_open_lesson(callback: types.CallbackQuery):
    await callback.message.delete()


# confirm of registering to open class
@dp.callback_query_handler(confirm_ol_cb.filter())
async def confirm_to_open_lesson(callback: types.CallbackQuery):
    course = confirm_ol_cb.parse(callback.data)['submenu']
    user = await db.select_user(id=callback.from_user.id)
    text = f"""
Клиент: {callback.from_user.mention} 
Записался на открытый урок по *{course.title()}*
Телефон клиента: {user[4]}
Имя клиента: {user[1]}
Дата отправки: {datetime.now().strftime("%d.%m.%Y %H:%M")}"""

    for manager in admins:
        await callback.bot.send_message(chat_id=manager,text=text, parse_mode=ParseMode.MARKDOWN)

    await callback.message.answer(text=await _("open_lesson_confirm"))
    await callback.message.delete()



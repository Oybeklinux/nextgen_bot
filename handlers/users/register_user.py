from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode, ContentType

from handlers.users.course import send_main_menu
from keyboards import language_ikb, language_cb, phone_kb, main_kb
from loader import dp, db


@dp.callback_query_handler(language_cb.filter())
async def back_to_course(callback: types.CallbackQuery) -> None:
    language = language_cb.parse(callback.data)['language']
    db.update_user(id=callback.from_user.id, language=int(language))

    await callback.message.answer(text=f"Отправьте пожалуйста ваш номер нажимая кнопку *Отправить номер*",
                            parse_mode=ParseMode.MARKDOWN,
                            reply_markup=phone_kb
                            )


@dp.message_handler(content_types=[ContentType.CONTACT])
async def get_contact(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    db.update_user(id=message.from_user.id, phone=phone)
    await message.answer(text="Введите имя пожалуйста")
    await state.set_state('name')


@dp.message_handler(state='name')
async def get_name(message: types.Message, state: FSMContext):
    name = message.text
    db.update_user(id=message.from_user.id, name=name)
    await message.answer(text='Вы успешно зарегистрированы!', reply_markup=main_kb)
    await send_main_menu(message)
    await state.finish()



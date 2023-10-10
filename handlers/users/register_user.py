from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode, ContentType
from data.texts import Texts
from keyboards import language_cb, get_phone_kb, get_main_kb
from keyboards.default.settings import get_settings_kb
from loader import dp, db


@dp.callback_query_handler(language_cb.filter(), state=None)
async def back_to_course(callback: types.CallbackQuery) -> None:
    language = language_cb.parse(callback.data)['language']
    db.update_user(id=callback.from_user.id, language=language)
    Texts.set_language(language)
    await callback.message.answer(text=Texts.get("send_phone"),
                            parse_mode=ParseMode.MARKDOWN,
                            reply_markup=get_phone_kb()
                            )

@dp.message_handler(content_types=[ContentType.CONTACT])
async def phone_to_settings(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if message.content_type is ContentType.CONTACT:
        phone = message.contact.phone_number
    elif message.content_type is ContentType.TEXT:
        import re
        phone = message.text.replace(' ', '').replace('+','')
        if not re.match('\d{12}|\d{9}', phone):
           await message.answer('Номер телефона должен состоять из 9 или 12 цифр. Введите заново')
           return

    if db.is_user_registered(user_id):
        await message.answer(text='Ваш номер успешно изменен!', reply_markup=get_settings_kb())
        await state.finish()
    else:
        await message.answer(text=Texts.get('tinput_name'))
        await state.set_state('name')
    db.update_user(id=user_id, phone=phone)


@dp.message_handler(state='name')
async def get_name(message: types.Message, state: FSMContext):
    name = message.text
    db.update_user(id=message.from_user.id, name=name)
    await message.answer(text=Texts.get('tsignup_info'), reply_markup=get_main_kb())
    # await send_main_menu(message)
    await state.finish()



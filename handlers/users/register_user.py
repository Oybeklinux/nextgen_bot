from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode, ContentType

from data.texts import _
from keyboards import language_cb, get_phone_kb, get_main_kb
from keyboards.default.settings import get_settings_kb
from loader import dp, db
from utils.set_bot_commands import set_default_commands


@dp.callback_query_handler(language_cb.filter(), state=None)
async def back_to_course(callback: types.CallbackQuery) -> None:
    language = language_cb.parse(callback.data)['language']
    await db.update_user(id=callback.from_user.id, language=language)
    await set_default_commands(dp)
    await callback.message.answer(text=await _("send_phone"),
                            parse_mode=ParseMode.MARKDOWN,
                            reply_markup=await get_phone_kb()
                            )


@dp.message_handler(content_types=[ContentType.CONTACT])
async def phone_to_settings(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if message.content_type is ContentType.CONTACT:
        phone = message.contact.phone_number
    # elif message.content_type is ContentType.TEXT:
    #     import re
    #     phone = message.text.replace(' ', '').replace('+','')
    #     if not re.match('\d{12}|\d{9}', phone):
    #        await message.answer(Texts().get('warn_phone_len'))
    #        return

    if await db.is_user_registered(user_id):
        await message.answer(text=await _('phone_edit_ok'), reply_markup=await get_settings_kb())
        await state.finish()
    else:
        await message.answer(text=await _('tinput_name'), reply_markup=types.ReplyKeyboardRemove())
        await state.set_state('name')
    await db.update_user(id=user_id, phone=phone)


@dp.message_handler(state='name')
async def get_name(message: types.Message, state: FSMContext):
    name = message.text
    await db.update_user(id=message.from_user.id, name=name)
    await message.answer(text=await _('tsignup_info'), reply_markup=await get_main_kb())
    # await send_main_menu(message)
    await state.finish()



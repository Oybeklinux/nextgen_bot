from aiogram import types

from loader import dp, db


# Главное -> Курсы 💻 -> Поиск
@dp.inline_handler(text='')
async def search(query: types.InlineQuery):
    rows = await db.select_courses(inline_mode=True)
    results = []
    for row in rows:
        results.append(
            types.InlineQueryResultArticle(
                id=row[0],
                title=row[4],
                thumb_url=row[2],
                description=row[3],
                input_message_content=types.InputTextMessageContent(
                    message_text=f'course_{row[1]}#'
                )
            )
        )

    await query.answer(results, cache_time=1, is_personal=True)
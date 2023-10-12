from aiogram import types

from data.texts import Texts


async def set_default_commands(dp):
        await dp.bot.set_my_commands([
            types.BotCommand("start", Texts.get('lstart')),
            types.BotCommand("help", Texts.get('lhelp')),
            types.BotCommand("courses", Texts.get('lcourses')),
            types.BotCommand("settings", Texts.get('lsettings')),
        ])

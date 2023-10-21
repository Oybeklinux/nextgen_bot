from aiogram import types

from data.texts import _


async def set_default_commands(dp):
        await dp.bot.set_my_commands([
            types.BotCommand("start", await _('lstart')),
            types.BotCommand("help", await _('lhelp')),
            types.BotCommand("courses", await _('lcourses')),
            types.BotCommand("settings", await _('lsettings')),
        ])

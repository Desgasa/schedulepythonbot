from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp
from app import db

import logging

logging.basicConfig(level=logging.INFO)

@dp.message_handler(CommandHelp())
async def help(call: types.Message):
        if(not db.subscriber_exests(call.from_user.id)):
                await call.answer("Сперва нужно добавить твои данные в базу.\nДля детальной информации напиши /info")
        else:        
            text = ("Список команд: ",
            "/start - Начать диалог",
            "/info - Информация про бота"
            "/help - Получить справку",
            "/time - Получить время пар",
            "/sendschedule - Получить расписание",
            "/sendplan - Получить план обучения")

            await call.answer("\n".join(text))
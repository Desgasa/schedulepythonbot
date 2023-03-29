from aiogram import types
from loader import dp
from app import db
import logging


logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands = ['time'],commands_prefix = "/!")
async def time(call: types.Message):
        if(not db.subscriber_exests(call.from_user.id)):
                await call.answer("Сперва нужно добавить твои данные в базу.\nДля детальной информации напиши /info")
        else:        
            text = ("1 пара  08-30 - 10-05",
            "2 пара  10-25 - 12-00",
            "3 пара  12-20 - 13-55",
            "4 пара  14-15 - 15-50",
            "5 пара  16-10 - 17-45")
            await call.answer("\n".join(text))
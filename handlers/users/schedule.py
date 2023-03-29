from aiogram import types
from loader import dp
from app import db
import logging


logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands = ['schedule'],commands_prefix = "/!")
async def info(call: types.Message):
    if(not db.subscriber_exests(call.from_user.id)):
        await call.answer("Сперва нужно добавить твои данные в базу.\nДля детальной информации напиши /info")
    else:
        kb = [
            [types.KeyboardButton(text="Первая неделя")],
            [types.KeyboardButton(text="Вторая неделя")]]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, one_time_keyboard=True)
        await call.answer("Выбери какая нужна неделя",reply_markup=keyboard)




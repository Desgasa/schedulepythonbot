from aiogram import types
from loader import dp
import logging


logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands = ['info'],commands_prefix = "/!")
async def info(call: types.Message):
    await call.answer("Данный бот сделан для помощи вам с вашим расписанием.\nДля работы с ботом нужно передать ваши данные, а именно вашу группу")
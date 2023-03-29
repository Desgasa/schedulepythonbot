from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from app import db
import logging


logging.basicConfig(level=logging.INFO)

 

@dp.message_handler(CommandStart())
async def start(call: types.Message):
        if(not db.subscriber_exests(call.from_user.id)):
            gif = open("Hello/hello.mp4",'rb')
            await call.answer_video(gif,caption="Приветствую\u2764\ufe0f!\nДля продолжения работы с ботом укажи группу в которой ты учишься")
        else:
            gif = open("Hello/hello.mp4",'rb')
            await call.answer_video(gif,caption="Приветствую\u2764\ufe0f!\nДанный бот сделан для того что бы упростить вам обучение")



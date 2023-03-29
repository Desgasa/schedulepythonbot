from aiogram import types
from loader import dp
from app import db
import os
from config import datas
import logging

logging.basicConfig(level=logging.INFO)




@dp.message_handler()
async def messagewrite(message: types.Message):
        if(not db.subscriber_exests(message.from_user.id)):
            for element in datas.groups:
                  if message.text.capitalize() == element:
                    db.add_subscriber(message.from_user.id,message.text.capitalize())
                    await message.reply("Данные добавленны в базу")
        if message.text.capitalize() == "Первая неделя":
            kb = [[types.KeyboardButton(text="Вернуться назад к выбору недели")]]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, one_time_keyboard=True)
            result = db.group_exests(message.from_user.id)
            group = result[0]
            cheak = open("C:\Python\\topbot\\Schedule\\" + group + "\\FirstWeek.png", 'rb')
            await message.answer_document(cheak, caption="Расписание на первую неделю",reply_markup=keyboard)
        if message.text.capitalize() == "Вторая неделя":
            kb = [[types.KeyboardButton(text="Вернуться назад к выбору недели")]]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, one_time_keyboard=True)
            result = db.group_exests(message.from_user.id)
            group = result[0]
            cheak = open("C:\Python\\topbot\\Schedule\\" + group + "\\SecondWeek.png", 'rb')
            await message.answer_document(cheak, caption="Расписание на вторую неделю",reply_markup=keyboard)
        if message.text.capitalize() == "Вернуться назад к выбору недели":
            kb = [
            [types.KeyboardButton(text="Первая неделя")],
            [types.KeyboardButton(text="Вторая неделя")]]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, one_time_keyboard=True)
            await message.answer("Выбери какая нужна неделя",reply_markup=keyboard)     
        if message.text.capitalize() == "Получить план на курс":
            kb = [
            [types.KeyboardButton(text="Первый курс")],
            [types.KeyboardButton(text="Второй курс")],
            [types.KeyboardButton(text="Третий курс")],
            [types.KeyboardButton(text="Четвертый курс")]]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, one_time_keyboard=True)
            await message.answer("Выбери нужный курс",reply_markup=keyboard)  
        try:
                if message.text.capitalize() == "Первый курс":
                    result = db.get_document(message.from_user.id)
                    file_name = result[0]
                    group = result[1]
                    file_path = "C:\Python\\topbot\\plangroup\\" + "Первый курс" + "\\" + group + "\\" + file_name
                    doc = open(file_path, "rb")
                    await message.answer_document(doc,caption="Вот твой план на выбранный курс")
                elif message.text.capitalize() == "Второй курс":
                    result = db.get_document2(message.from_user.id)
                    file_name = result[0]
                    group = result[1]
                    file_path = "C:\Python\\topbot\\plangroup\\" + "Второй курс" + "\\" + group + "\\" + file_name
                    doc = open(file_path, "rb")
                    await message.answer_document(doc,caption="Вот твой план на выбранный курс")   
                elif message.text.capitalize() == "Третий курс":
                    result = db.get_document3(message.from_user.id)
                    file_name = result[0]
                    group = result[1]
                    file_path = "C:\Python\\topbot\\plangroup\\" + "Третий курс" + "\\" + group + "\\" + file_name
                    doc = open(file_path, "rb")
                    await message.answer_document(doc,caption="Вот твой план на выбранный курс")   
                elif message.text.capitalize() == "Четвертый курс":
                    result = db.get_document4(message.from_user.id)
                    file_name = result[0]
                    group = result[1]
                    file_path = "C:\Python\\topbot\\plangroup\\" + "Четвертый курс" + "\\" + group + "\\" + file_name
                    doc = open(file_path, "rb")
                    await message.answer_document(doc,caption="Вот твой план на выбранный курс")                      
        except:
             await message.answer("Сначала загрузи файл")                
from aiogram import Bot, Dispatcher, executor, types
from loader import dp
from loader import bot
from config import datas
from os import path
import shutil
from app import db


import logging

logging.basicConfig(level=logging.INFO)


@dp.message_handler(content_types=["document"])
async def download_document(message: types.Message):
            if "Первый курс" in message.document.file_name:
                if message.caption.capitalize() in datas.groups:
                    db.add_document(message.from_user.id,message.document.file_name,message.document.file_id, message.caption.capitalize())
                    file_id = message.document.file_id
                    file = await bot.get_file(file_id)
                    await bot.download_file(file.file_path, message.document.file_name)
                    source_path = "C:\Python\\topbot\\" + message.document.file_name
                    if path.exists(source_path):
                        destination_path = "C:\Python\\topbot\\plangroup\\"+ "Первый курс" + "\\" + message.caption.capitalize() + "\\" + message.document.file_name
                        shutil.move(source_path, destination_path)
            elif "Второй курс" in message.document.file_name:
                if message.caption.capitalize() in datas.groups:
                    db.add_document2(message.from_user.id,message.document.file_name,message.document.file_id, message.caption.capitalize())
                    file_id = message.document.file_id
                    file = await bot.get_file(file_id)
                    await bot.download_file(file.file_path, message.document.file_name)
                    source_path = "C:\Python\\topbot\\" + message.document.file_name
                    if path.exists(source_path):
                        destination_path = "C:\Python\\topbot\\plangroup\\"+ "Второй курс" + "\\" + message.caption.capitalize() + "\\" + message.document.file_name
                        shutil.move(source_path, destination_path)
            elif "Третий курс" in message.document.file_name:
                if message.caption.capitalize() in datas.groups:
                    db.add_document3(message.from_user.id,message.document.file_name,message.document.file_id, message.caption.capitalize())
                    file_id = message.document.file_id
                    file = await bot.get_file(file_id)
                    await bot.download_file(file.file_path, message.document.file_name)
                    source_path = "C:\Python\\topbot\\" + message.document.file_name
                    if path.exists(source_path):
                        destination_path = "C:\Python\\topbot\\plangroup\\"+ "Третий курс" + "\\" + message.caption.capitalize() + "\\" + message.document.file_name
                        shutil.move(source_path, destination_path)
            elif "Четвертый курс" in message.document.file_name:
                if message.caption.capitalize() in datas.groups:
                    db.add_document4(message.from_user.id,message.document.file_name,message.document.file_id, message.caption.capitalize())
                    file_id = message.document.file_id
                    file = await bot.get_file(file_id)
                    await bot.download_file(file.file_path, message.document.file_name)
                    source_path = "C:\Python\\topbot\\" + message.document.file_name
                    if path.exists(source_path):
                        destination_path = "C:\Python\\topbot\\plangroup\\"+ "Четвертый курс" + "\\" + message.caption.capitalize() + "\\" + message.document.file_name
                        shutil.move(source_path, destination_path)                        
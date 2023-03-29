from utils.set_bot_commands import set_default_commands
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import maindb


db = maindb.SQLighter('db.db')
async def on_startup(dp):
    
    await set_default_commands(dp)

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    
    

    executor.start_polling(dp, on_startup=on_startup)
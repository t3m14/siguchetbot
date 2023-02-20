from aiogram import Dispatcher
from aiogram.types import Message
from ..keyboards.reply import main_menu


async def user_start(message: Message):
    await message.reply("Привет! Выбери нужный тебе пункт меню", reply_markup=main_menu)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")

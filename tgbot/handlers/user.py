from aiogram import Dispatcher
from aiogram.types import Message
from ..keyboards.reply import main_menu
from ..models.database_operations import create_user_if_not_exists

async def user_start(message: Message):
    create_user_if_not_exists(message.from_user.id)
    await message.reply("Привет! Выбери нужный тебе пункт меню", reply_markup=main_menu)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from ..keyboards.inline import cancel_add

async def reply(message: Message):
    if message:
        await message.delete()
        if message.text == "+1":
            random_frase = "Выкуренно ещё на одну сигаретку больше("
            await message.answer(f"{random_frase}\nЕсли вы нажали по ошибке всегда можно нажать на кнопку снизу", reply_markup=cancel_add)
        if message.text == "Статистика":
            print("Статистика")
        if message.text == "Профиль":
            print("Профиль")


async def inline(call: CallbackQuery):
    if call.data == "minus_one":
        await call.message.delete()
        print("-1")


def register_buttons(dp: Dispatcher):
    dp.register_callback_query_handler(inline, state="*")
    dp.register_message_handler(
        reply, state="*")

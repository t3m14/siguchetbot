from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from ..keyboards.inline import cancel_add
from ..models.database_operations import add_counter, reduse_counter, get_today_counter
async def reply(message: Message):
    if message:
        await message.delete()
        if message.text == "+1":
            add_counter(message.from_user.id)
            random_frase = "Выкуренно ещё на одну сигаретку больше("
            await message.answer(f"{random_frase}\nЕсли вы нажали по ошибке всегда можно нажать на кнопку снизу", reply_markup=cancel_add)
        if message.text == "Статистика":
            statistic = f"Ваша статистика\nЗа сегодня: {get_today_counter(message.from_user.id)}\nЗа вчера: {}\nЗа месяц {}"
            await message.answer()
        if message.text == "Профиль":
            print("Профиль")


async def inline(call: CallbackQuery):
    await call.message.delete()
    if call.data == "minus_one":
        reduse_counter(call.from_user.id)
        print("-1")


def register_buttons(dp: Dispatcher):
    dp.register_callback_query_handler(inline, state="*")
    dp.register_message_handler(
        reply, state="*")

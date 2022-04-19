import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar

API_TOKEN = ''

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

start_kb = ReplyKeyboardMarkup(resize_keyboard=True,)
start_kb.row('Навигационный календарь', 'Диалоговый календарь').row("Поддержать автора")


# starting bot when user sends `/start` command, answering with inline calendar
@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    await message.reply('Привет 🖐\n\n Этот бот был создан для учёта рациона потребления табака 🚬\n\n Бот пока находится в разработке и мы очень надеемся, что вскоре он поможет изменить вашу жизнь к лучшему 🐱‍\n\n Целью этого бота является показать пользователю как часто он употребляет табак, что помогло бы контролировать его курение. \n\nБот полностью бесплатный, но вы можете всегда поблагодарить автора. 🐱‍👤', reply_markup=start_kb)


@dp.message_handler(Text(equals=['Навигационный календарь'], ignore_case=True))
async def nav_cal_handler(message: Message):
    await message.answer("Пожалуйста, выберете дату: ", reply_markup=await SimpleCalendar().start_calendar())


# simple calendar usage
@dp.callback_query_handler(simple_cal_callback.filter())
async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.answer(
            f'Вы выбрали {date.strftime("%d/%m/%Y")}',
            reply_markup=start_kb
        )


@dp.message_handler(Text(equals=['Диалоговый календарь'], ignore_case=True))
async def simple_cal_handler(message: Message):
    await message.answer("Пожалуйста, выберете дату: ", reply_markup=await DialogCalendar().start_calendar())


# dialog calendar usage
@dp.callback_query_handler(dialog_cal_callback.filter())
async def process_dialog_calendar(callback_query: CallbackQuery, callback_data: dict):
    selected, date = await DialogCalendar().process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.answer(
            f'You selected {date.strftime("%d/%m/%Y")}',
            reply_markup=start_kb
        )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)   

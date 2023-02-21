from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cancel_add = InlineKeyboardMarkup().add(InlineKeyboardButton("Отмена", callback_data="minus_one")).add(InlineKeyboardButton("Закрыть ❌", callback_data="close"))

close = InlineKeyboardMarkup().add(InlineKeyboardButton("Закрыть ❌", callback_data="close"))
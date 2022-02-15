from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import buy_callback
choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data=""),
            InlineKeyboardButton(test="Нет", callback_data=""),
        ],
        [
            InlineKeyboardButton(text="Отмена",callback_data="cancel")
        ]
    ]

)
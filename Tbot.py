import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types

Token = '5209932574:AAFJpNe9bt1fhMma-jwGNP5YSoGJqWjcrh8'
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Будешь сегодня кушать?', reply_markup=gen_marcup())


def main():
    bot.polling()


def gen_marcup():
    marcup = InlineKeyboardMarkup()
    marcup.row_width = 2
    marcup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
               InlineKeyboardButton("No", callback_data="cb_no"))
    return marcup


#
# @bot.message_handler(commands=['switch'])
# def switch(message):
#     markup = types.InlineKeyboardMarkup()
#     switch_button = types.InlineKeyboardButton(text='Try', switch_inline_query="Telegram")
#     markup.add(switch_button)
#     bot.send_message(message.chat.id, "Выбрать чат", reply_markup = markup)
#


# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
#
main()

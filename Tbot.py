import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import qrcode
import random
import os
import datetime

Token = '5209932574:AAFJpNe9bt1fhMma-jwGNP5YSoGJqWjcrh8'
bot = telebot.TeleBot(Token)

name = ""
surname = ""
grade = ""
day = ""

number = random.randrange(1000, 5000)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')
    bot.send_message(message.from_user.id, "Как тебя зовут?")
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'С какого ты класса?(цифрами пожалуйста)')
    bot.register_next_step_handler(message, get_grade)


def get_grade(message):
    global grade
    grade = message.text
    question = 'Ты с ' + str(grade) + ' класса, тебя зовут ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=gen_marcup_for_approve_name())


def gen_marcup_for_approve_name():
    marcup = InlineKeyboardMarkup()
    marcup.row_width = 2
    marcup.add(InlineKeyboardButton("Да", callback_data="cb_yes"),
               InlineKeyboardButton("Нет", callback_data="cb_no"))
    return marcup


def gen_marcup_for_change_data():
    marcup = InlineKeyboardMarkup()
    marcup.row_width = 2
    marcup.add(InlineKeyboardButton("Начать заново", callback_data="back"),
               InlineKeyboardButton("Нет, все в порядке", callback_data="no_wont_change"))
    return marcup

# def get_number():
#     number = random.randrange(1000, 5000)    ДОПИСАТЬ!
#


def get_day():
    global day
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    day = year+month+day+time


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "cb_no":
        bot.send_message(call.message.chat.id, "Изменить свои данные", reply_markup=gen_marcup_for_change_data())
    elif call.data == "cb_yes":
        bot.send_message(call.message.chat.id, 'Запомню : )')
        bot.send_message(call.message.chat.id, 'Вот меню на сегодня:'
                                               'Салат из квашенной капусты с маслом растительным;'
                                               'Суп картофельный с горохом и гренками;'
                                               'Биточки, рубленные из птицы;'
                                               'Каша гречневая рассыпчатая;'
                                               'Сок фруктовый;'
                                               'Фрукты свежие;'
                                               'Батон или хлеб')
        bot.send_message(call.message.chat.id, 'Будешь сегодня кушать?', reply_markup=gen_marcup())

    if call.data == "yes_will_eat":
        bot.answer_callback_query(call.id, "Вот твой QR-код")
        users = surname + " " + name + "/" + grade + "/" + day + "/" + "2334"
        img = qrcode.make(users)
        img.save('qr_code.png')
        bot.send_photo(call.message.chat.id, open('qr_code.png', 'rb'))
    elif call.data == "no_wont_eat":
        bot.answer_callback_query(call.id, "Хорошо, до завтра.")

    if call.data == "no_wont_change":
        bot.answer_callback_query(call.id, "Хорошо, пойдем дальше")
        bot.send_message(call.message.chat.id, 'Вот меню на сегодня:'
                                               'Салат из квашенной капусты с маслом растительным;'
                                               'Суп картофельный с горохом и гренками;'
                                               'Биточки, рубленные из птицы;'
                                               'Каша гречневая рассыпчатая;'
                                               'Сок фруктовый;'
                                               'Фрукты свежие;'
                                               'Батон или хлеб')
        bot.send_message(call.message.chat.id, 'Будешь сегодня кушать?', reply_markup=gen_marcup())
    elif call.data == "back":
        bot.send_message(call.message.chat.id, "Введи свои имя, фамилию и класс заново")
        question = 'Ты с ' + str(grade) + ' класса, тебя зовут ' + name + ' ' + surname + '?'
        bot.send_message(call.message.chat.id, "Как тебя зовут?")

        # global name
        # name = message.chat.id.text
        # bot.send_message(call.message.from_user.id, text=question, reply_markup=gen_marcup_for_vary_data())

    bot.answer_callback_query(call.id)


def gen_marcup():
    marcup = InlineKeyboardMarkup()
    marcup.row_width = 2
    marcup.add(InlineKeyboardButton("Да", callback_data="yes_will_eat"),
               InlineKeyboardButton("Нет", callback_data="no_wont_eat"))
    return marcup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Вот твой QR-код")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Хорошо, до завтра.")


def main():
    get_day()
    bot.polling()



# number = random.randrange(1000, 5000))


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

# today = date.today()

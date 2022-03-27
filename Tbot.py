import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import qrcode
import random
import datetime
import sqlite3

Token = '5209932574:AAFJpNe9bt1fhMma-jwGNP5YSoGJqWjcrh8'
bot = telebot.TeleBot(Token)
name = ""
surname = ""
grade = ""
day = ""
second_name = ""
grade_level = ""
patronymic = ""

connection = sqlite3.connect('progect.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS progect 
              (Surname TEXT, Name TEXT, Class INT, id INT)''')
cursor.execute("DELETE FROM progect")


# print(cursor.execute("SELECT * FROM progect").fetchall())


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')
    bot.send_message(message.from_user.id, "Как тебя зовут?(ФИО)")
    bot.send_message(message.from_user.id, 'С какого ты класса?')
    bot.register_next_step_handler(message, get_grade)


def get_grade(message):
    global grade
    grade = message.text
    question = str(grade)
    bot.send_message(message.from_user.id, text=question, reply_markup=gen_marcup_for_approve_name(message))


def gen_marcup_for_approve_name(message):
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


def get_day():
    global day
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    day = year + month + day + time


def get_number():
    number = random.randint(1000, 5000)
    x = str(number)
    return x


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "cb_no":
        bot.send_message(call.message.chat.id, "Изменить свои данные", reply_markup=gen_marcup_for_change_data())
    elif call.data == "cb_yes":
        bot.send_message(call.message.chat.id, 'Запомню : )')
        bot.send_message(call.message.chat.id, 'Вот меню на сегодня:                                      '
                                               '                                 '
                                               '○Салат из квашенной капусты с маслом растительным;       '
                                               '                                                                  '
                                               '○Суп картофельный с горохом и гренками;                         '
                                               '○Биточки, рубленные из птицы;                                          '
                                               '○Каша гречневая рассыпчатая;                                           '
                                               '○Сок фруктовый;                                                        '
                                               '○Фрукты свежие;                                                        '
                                               '○Батон или хлеб')
        bot.send_message(call.message.chat.id, 'Будешь сегодня кушать?', reply_markup=gen_marcup())

    if call.data == "yes_will_eat":
        bot.answer_callback_query(call.id, "Вот твой QR-код")
        users = surname + " " + name + "/" + grade + "/" + day + "/" + get_number()
        img = qrcode.make(users)
        img.save('qr_code.png')
        bot.send_photo(call.message.chat.id, open('qr_code.png', 'rb'))
    elif call.data == "no_wont_eat":
        bot.answer_callback_query(call.id, "Хорошо, до завтра:)")
    if call.data == "no_wont_change":
        bot.answer_callback_query(call.id, "Хорошо, пойдем дальше")
        bot.send_message(call.message.chat.id, 'Вот меню на сегодня:                                      '
                                               '                                 '
                                               '○Салат из квашенной капусты с маслом растительным;       '
                                               '                                                                  '
                                               '○Суп картофельный с горохом и гренками;                         '
                                               '○Биточки, рубленные из птицы;                                          '
                                               '○Каша гречневая рассыпчатая;                                           '
                                               '○Сок фруктовый;                                                        '
                                               '○Фрукты свежие;                                                        '
                                               '○Батон или хлеб')
        bot.send_message(call.message.chat.id, 'Будешь сегодня кушать?', reply_markup=gen_marcup())
    elif call.data == "back":
        get_restart(call.message)

    elif call.data == 'yes_swap_name':
        bot.answer_callback_query(call.id, "Хорошо, пойдем дальше")
        bot.send_message(call.message.chat.id, 'Вот меню на сегодня:                                      '
                                               '                                 '
                                               '○Салат из квашенной капусты с маслом растительным;       '
                                               '                                                                  '
                                               '○Суп картофельный с горохом и гренками;                         '
                                               '○Биточки, рубленные из птицы;                                          '
                                               '○Каша гречневая рассыпчатая;                                           '
                                               '○Сок фруктовый;                                                        '
                                               '○Фрукты свежие;                                                        '
                                               '○Батон или хлеб')
        bot.send_message(call.message.chat.id, 'Будешь сегодня кушать?', reply_markup=gen_marcup())


def get_restart(message):
    bot.send_message(message.chat.id, "Как тебя зовут?")
    bot.register_next_step_handler(message, get_second_name)


def get_second_name(message):
    global second_name
    second_name = message.text
    bot.send_message(message.chat.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_patronymic)


def get_patronymic(message):
    global patronymic
    patronymic = message.text
    bot.send_message(message.chat.id, 'С какого ты класса?')
    bot.register_next_step_handler(message, get_grade_level)


def get_grade_level(message):
    global grade_level
    grade_level = message.text
    question = 'Ты с ' + str(grade_level) + ' класса, тебя зовут ' + second_name + ' ' + patronymic + '?'
    bot.send_message(message.chat.id, text=question, reply_markup=gen_marcup_for_swap_name())


def gen_marcup_for_swap_name():
    marcup = InlineKeyboardMarkup()
    marcup.row_width = 1
    marcup.add(InlineKeyboardButton("Да", callback_data="yes_swap_name"))
    return marcup


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


main()

import telebot
import sqlite3

bot = telebot.TeleBot('5209932574:AAFJpNe9bt1fhMma-jwGNP5YSoGJqWjcrh8')

@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS nickname(
        id INTEGER
    )""")
    connect.commit()


    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM users.db WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        students_list = [message.chat.id]
        cursor.execute("INSERT INTO nickname VALUES(?);", students_list)
        connect.commit()
    else:
        bot.send_message(message.chat.id, 'Такой пользователь уже существует')


@bot.message_handler(commands=['delete'])
def delete(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    people_id = message.chat.id
    cursor.execute(f"DELETE FROM nickname WHERE id = {people_id}")
    connect.commit()



bot.polling()
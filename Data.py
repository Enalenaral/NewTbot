import sqlite3

@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
   id  INTEGER
    )""")

    connect.commit()

    user_id = [message.chat.id]
    cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
    connect.commit()

    people_id = message.chat.id
    cursor.execute("SELECT id FROM login_id WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login _id VALUES(?);", user_id)
        connect.commit()
    else:
        bot.send_message(message.chat.id, '...')


@bot.message_handler(commands=['delete'])
def delete(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()


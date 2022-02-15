import telebot


bot = telebot.TeleBot('5209932574:AAFJpNe9bt1fhMma-jwGNP5YSoGJqWjcrh8')

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Ты будешь сегодня кушать?')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

bot.polling(none_stop=True, interval=0)
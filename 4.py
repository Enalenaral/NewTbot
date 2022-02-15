# @bot.message_handler(commands="start")
# async def cmd_start(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup()
#     button_1 = types.KeyboardButton(text="С пюрешкой")
#     keyboard.add(button_1)
#     button_2 = "Без пюрешки"
#     keyboard.add(button_2)
#     await message.answer("Как подавать котлеты?", reply_markup=keyboard)
#
#     @bot.message_handler(commands="inline_url")
#     async def cmd_inline_url(message: types.Message):
#         buttons = [
#             types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
#             types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
#         ]
#         keyboard = types.InlineKeyboardMarkup(row_width=2)
#         keyboard.add(*buttons)
#         await message.answer("Кнопки-ссылки", reply_markup=keyboard)
# # @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет! Ты будешь сегоднaя кушать?')





@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Вот ваш QR-код")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Хорошо, до завтра.")

@bot.message_handler(func=lambda message: True)
def messange_handler(message):
    bot.send_message(message.chat.id, "Yes/No", reply_markup=gen_marcup())

bot.infinity_polling()

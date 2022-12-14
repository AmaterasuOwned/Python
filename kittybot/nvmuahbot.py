import telebot


token = "5334912797:AAFpYMe5Po23KD8_k7s_PEpUtMH0E3w_bUU"
bot = telebot.Telebot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_poling()

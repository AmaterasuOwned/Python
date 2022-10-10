from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler


updater = Updater(token="5334912797:AAFpYMe5Po23KD8_k7s_PEpUtMH0E3w_bUU")


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привет, я KittyBot!")


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([
                ['Который час?', 'Определи мой ip'],
                ['/random_digit']
            ])
    context.bot.send_message(
        chat_id=chat.id,
        text="Спасибо, что включили меня,{}!".format(name),
        reply_markup=buttons,
    )


bot = Bot(token="5334912797:AAFpYMe5Po23KD8_k7s_PEpUtMH0E3w_bUU")

updater.dispatcher.add_handler(CommandHandler("start", wake_up))

updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling(poll_interval=15.0)
updater.idle()

import requests
import os

from dotenv import load_dotenv

from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler

load_dotenv()

secret_token = os.getenv('TOKEN')

updater = Updater(token=secret_token)
URL = 'https://api.thecatapi.com/v1/images/search'


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привет, я KittyBot!")


def get_new_image():
    response = requests.get(URL).json()
    random_cat = response[0].get('url')
    return random_cat


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text="Привет, {}. Посмотри, какого котика я тебе нашёл".format(name),
        reply_markup=button,
    )


bot = Bot(token=secret_token)

updater.dispatcher.add_handler(CommandHandler("start", wake_up))

updater.dispatcher.add_handler(MessageHandler(Filters.text, new_cat))

updater.start_polling(poll_interval=15.0)
updater.idle()

import requests
from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler


updater = Updater(token="5334912797:AAFpYMe5Po23KD8_k7s_PEpUtMH0E3w_bUU")
URL = "https://api.thecatapi.com/v1/images/search"


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text="Привет, я бот Натальи @NVMuah <- нажми  для связи с мастером !",
    )


def get_new_image():
    response = requests.get(URL).json()
    random_cat = response[0].get("url")
    return random_cat


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def photo(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/Photo']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text="{},больше фото смотри на"
        "https://vk.com/makeupbynatalia и "
        "https://www.instagram.com/nvmuah/ ".format(name),
        reply_markup=button,
    )


bot = Bot(token="5334912797:AAFpYMe5Po23KD8_k7s_PEpUtMH0E3w_bUU")

updater.dispatcher.add_handler(CommandHandler("Photo", photo))

updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling(poll_interval=15.0)
updater.idle()

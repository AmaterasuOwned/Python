import requests
import os

from dotenv import load_dotenv

from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler


load_dotenv()

secret_token = os.getenv('TOKEN')

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
        text="{}, портфолио : "
        "http://nvmuah.tilda.ws/".format(name),
        reply_markup=button,
    )


def booking(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/Booking']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text="{}, выберите дату для записи".format(name),
        reply_markup=button,
    )


bot = Bot(token=secret_token)


def main():
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', say_hi))
    updater.dispatcher.add_handler(CommandHandler('Photo', photo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

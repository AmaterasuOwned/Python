import requests

from telegram import Bot

bot = Bot(token='5334912797:AAFpYMe5Po23KD8_k7s_PEpUtMH0E3w_bUU')

URL = 'https://api.thecatapi.com/v1/images/search'

response = requests.get(URL).json()
random_cat_url = response[0].get('url')

chat_id = 58800473
text = 'а вот и я!'

bot.send_message(chat_id, text)
# Отправка изображения
bot.send_photo(chat_id, random_cat_url)

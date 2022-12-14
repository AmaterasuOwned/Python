
import telebot
import logging
from telebot import types
import config
from logging.handlers import RotatingFileHandler

bot = telebot.TeleBot(config.token)

formatter = logging.Formatter(
    "%(asctime)s, %(levelname)s, %(message)s, %(name)s"
)
logger = logging.getLogger("__name__")
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler("main.log", maxBytes=50000000, backupCount=5)
logger.addHandler(handler)
handler.setFormatter(formatter)


@bot.message_handler(commands=["start"])
def start(message):
    logging.info('Запускаем бота')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("Записаться")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id,
        text="Привет, {0.first_name}! Я бот Натальи @NVmuah".format(message.from_user),
        reply_markup=markup,
    )


@bot.message_handler()
def func(message):
    if message.text == "👋 Поздороваться" or "Привет" or "привет":
        bot.send_message(
            message.chat.id,
            text="Привет! Я Наталья @NVMuah\n"
            "Ваш гуру в мире макияжа\n"
            "Подробнее про меня можно узнать:\n"
            "Сайт http://nvmuah.tilda.ws/\n"
        )
        keyboard1 = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Instagram",
            url="https://www.instagram.com/nvmuah/"
        )
        keyboard1.add(url_button)
        bot.send_message(message.chat.id, 'Нажми 👇👇👇👇👇', reply_markup=keyboard1)
        keyboard2 = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Группа в VK",
            url="https://vk.com/makeupbynatalia"
        )
        keyboard2.add(url_button)
        bot.send_message(message.chat.id, 'Нажми 👇👇👇👇👇', reply_markup=keyboard2)
        keyboard3 = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Телеграмм канал",
            url="https://t.me/+Ghjrdtv5DtM4MGJi"
        )
        keyboard3.add(url_button)
        bot.send_message(message.chat.id, 'Нажми 👇👇👇👇👇', reply_markup=keyboard3)
    elif message.text == "Записаться":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Записаться на полный образ")
        btn2 = types.KeyboardButton("Записаться на макияж")
        btn3 = types.KeyboardButton("Записаться на укладку")
        btn4 = types.KeyboardButton("Записаться на обучение")
        btn5 = types.KeyboardButton("Записаться на свадебный образ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Выберите запись", reply_markup=markup)

    elif message.text == "Записаться на полный образ":
        img = open("E:\Dev\Bot\Photo_bot\Full.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(
            message.chat.id,
            text=(
                "Полный образ включает в себя\n"
                "Дневной или вечерний макияж\n"
                "Локоны или причёска\n"
                "Продолжительность - 2 часа\n\n"
                "Цена - 4500 руб."
            ),
        )
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Написать мастеру",
            url="https://api.whatsapp.com/send/?phone=79132004040&text&type=phone_number&app_absent=0"
        )
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Написать мастеру", reply_markup=keyboard)
    elif message.text == "образ":
        img = open("E:\Dev\Bot\Photo_bot\Full.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(
            message.chat.id,
            text=(
                "Полный образ включает в себя\n"
                "Дневной или вечерний макияж\n"
                "Локоны или причёска\n"
                "Продолжительность - 2 часа\n\n"
                "Цена - 4500 руб."
            ),
        )
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Написать мастеру",
            url="https://api.whatsapp.com/send/?phone=79132004040&text&type=phone_number&app_absent=0"
        )
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Написать мастеру", reply_markup=keyboard)
    elif message.text == "макияж и прическа":
        img = open("E:\Dev\Bot\Photo_bot\Full.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(
            message.chat.id,
            text=(
                "Полный образ включает в себя\n"
                "Дневной или вечерний макияж\n"
                "Локоны или причёска\n"
                "Продолжительность - 2 часа\n\n"
                "Цена - 4500 руб."
            ),
        )
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Написать мастеру",
            url="https://api.whatsapp.com/send/?phone=79132004040&text&type=phone_number&app_absent=0"
        )
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Написать мастеру", reply_markup=keyboard)
    elif message.text == "Записаться на макияж":
        img = open("E:\Dev\Bot\Photo_bot\MakeUp.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(
            message.chat.id,
            text=(
                "Дневной или вечерний макияж\n"
                "Продолжительность - 1 час\n"
                "Цена - 2500 руб.\n"
            ),
        )
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Написать мастеру",
            url="https://api.whatsapp.com/send/?phone=79132004040&text&type=phone_number&app_absent=0"
        )
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Написать мастеру", reply_markup=keyboard)
        img = open("E:\Dev\Bot\Photo_bot\MakeUp.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(
            message.chat.id,
            text=(
                "Дневной или вечерний макияж\n"
                "Продолжительность - 1 час\n"
                "Цена - 2500 руб.\n"
            ),
        )
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Написать мастеру",
            url="https://api.whatsapp.com/send/?phone=79132004040&text&type=phone_number&app_absent=0"
        )
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Написать мастеру", reply_markup=keyboard)
    elif message.text == "Записаться на укладку":
        img = open("E:\Dev\Bot\Photo_bot\hair.jpg", "rb")
        img2 = open("E:\Dev\Bot\Photo_bot\hair2.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_photo(message.chat.id, img2)
        bot.send_message(
            message.chat.id,
            text=(
                "Укладка\n\n"
                "Распушенные волосы с текстурой и прикорневым объемом:\n"
                "Локоны\n"
                "Голливудская волна\n"
                "Выпрямление на утюг\n"
                "Продолжительность - 40 минут\n\n"
                "Цена-1500₽\n\n"
                "Собранная причёска:\n\n"
                "Гладкий пучок\n"
                "Хвост\n"
                "Высокий или низкий пучок из локонов\n"
                "Продолжительность - 1 час 20 минут\n\n"
                "Цена-2000 руб.\n\n"
                )
        )
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Написать мастеру",
            url="https://api.whatsapp.com/send/?phone=79132004040&text&type=phone_number&app_absent=0"
        )
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Написать мастеру", reply_markup=keyboard)

        img = open("E:\Dev\Bot\Photo_bot\Wedding.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(
            message.chat.id,
            text=(
                "Обсуждение и выбор свадебного макияжа и прически\n"
                "Свадебный макияж\n"
                "Свадебная причёска\n"
                "Возможность выбрать украшения в причёску из имеющихся у мастера в ассортименте\n"
                "Помощь в сборах(шнуровка платья, закрепление фоты и других украшений)\n"
                "Возможность провести небольшую съёмку сборов, если Вас будет сопровождать фотограф\n\n"
                "Цена - 6000 руб.\n"
                "*выезд по городу 1000₽"
            ),
        )
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Написать мастеру",
            url="https://api.whatsapp.com/send/?phone=79132004040&text&type=phone_number&app_absent=0"
        )
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Написать мастеру", reply_markup=keyboard)    
    elif message.text == "Записаться на свадебный образ":
        img = open("E:\Dev\Bot\Photo_bot\Wedding.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(
            message.chat.id,
            text=(
                "Обсуждение и выбор свадебного макияжа и прически\n"
                "Свадебный макияж\n"
                "Свадебная причёска\n"
                "Возможность выбрать украшения в причёску из имеющихся у мастера в ассортименте\n"
                "Помощь в сборах(шнуровка платья, закрепление фоты и других украшений)\n"
                "Возможность провести небольшую съёмку сборов, если Вас будет сопровождать фотограф\n\n"
                "Цена - 6000 руб.\n"
                "*выезд по городу 1000₽"
            ),
        )
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Написать мастеру",
            url="https://api.whatsapp.com/send/?phone=79132004040&text&type=phone_number&app_absent=0"
        )
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Написать мастеру", reply_markup=keyboard)

    elif message.text == "Записаться на обучение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Макияж для себя")
        btn2 = types.KeyboardButton("Профессия визажист")
        btn3 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Выберите обучение", reply_markup=markup)
    elif message.text == "Профессия визажист":
        img = open("E:\Dev\Bot\Photo_bot\PT.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(
            message.chat.id,
            text=(
                "Курс Визажист PRO базовый\n "
                "Освой профессию визажиста!"
                "Индивидуальный курс\n"
                "Мы изучим самые актуальные технике в макияже:\n"
                "Nude - макияж без макияжа\n"
                "Свадебный\n"
                "Макияж на фотосессию\n"
                "Лифтинг- макияж\n"
                "Макияж в стиле Hollywood\n"
                "Smoke eyes\n"
                "На каждом занятие показ и отработка,\n"
                "модели и материалы предоставляются\n\n"
                "Цена - 35000 руб.\n"
                "Цена одного урока - 5000 руб.\n"
            ),
        )
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Написать мастеру",
            url="https://api.whatsapp.com/send/?phone=79132004040&text&type=phone_number&app_absent=0"
        )
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Написать мастеру", reply_markup=keyboard)

    elif message.text == "Макияж для себя":
        img = open("E:\Dev\Bot\Photo_bot\SSV.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(
            message.chat.id,
            text=(
                "Урок Макияж для себя офлайн:\n\n"
                "Индивидуальный урок\n"
                "Разбор вашей косметички\n"
                "Теоретическая часть\n"
                "Отработка макияжа по вашему запросу\n"
                "продолжительность 2,5 часа\n\n"
                "Цена - 2500 руб.\n\n"
                "Урок Макияж для себя онлайн:\n\n"
                "Индивидуальный урок\n"
                "Отработка дневного макияжа и трансформация в вечерний\n"
                "Продолжительность 1,5 часа\n\n"
                "Цена - 1500 руб.\n"
            ),
        )
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text="Написать мастеру",
            url="https://api.whatsapp.com/send/?phone=79132004040&text&type=phone_number&app_absent=0"
        )
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Написать мастеру", reply_markup=keyboard)

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        btn2 = types.KeyboardButton("Записаться")
        markup.add(btn1, btn2)
        bot.send_message(
            message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup
        )
    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Записаться на полный образ")
        btn2 = types.KeyboardButton("Записаться на макияж")
        btn3 = types.KeyboardButton("Записаться на укладку")
        btn4 = types.KeyboardButton("Записаться на обучение")
        btn5 = types.KeyboardButton("Записаться на свадебный образ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Выберите запись", reply_markup=markup)

    else:
        bot.send_message(
            message.chat.id, text="На такую комманду я не запрограммировал.."
        )


bot.polling(none_stop=True)

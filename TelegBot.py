import telebot
from extensions import Converter, ApiException, currency
from config import *
import traceback

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = 'Приветсвую в конверторе валют, для помощи введите /help'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['help'])
def start(message: telebot.types.Message):
    text = 'Введите текст формата [Валюта1] [Валюта2] [Количество]\nВалюта1 - из которой конвертируем' \
           ' \nдля списка валют введите команду /values'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values_info(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in currency.keys():
        text = '\n'.join((text, i))

    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def currency_ans(message: telebot.types.Message):
    values = message.text.split()
    try:
        if len(values) != 3:
            raise ApiException('Неверное количество параметров!')

        answer = Converter.get_price(*values)
    except ApiException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, answer)


bot.polling(none_stop=True)

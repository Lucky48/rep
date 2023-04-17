import telebot
from config import keys, TOKEN, tgTOKEN, currency
from utils import ConvertionException, CryptoConverter
bot = telebot.TeleBot(tgTOKEN)

@bot.message_handler(commands=["start", "help"])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу, введите команду боту в следующем формате: \n \
    <валюта> <в какую валюту перевести> <количество переводимой валюты>\nУвидеть список всех доступных валют: /list"
    bot.reply_to(message, text)

@bot.message_handler(commands=["list"])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in currency:
        text = "\n" .join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=["text", ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) != 3:
            raise ConvertionException("Слишком много параметров")

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f"Ошибка пользователя.\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:
        text = f"Цена {amount} {quote} в {base} - {total_base}"
        bot.send_message(message.chat.id, text)

    quote_ticker, base_ticker = keys[quote], keys[base]


bot.infinity_polling()
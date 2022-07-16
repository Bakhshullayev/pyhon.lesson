import telebot
from transliterate import to_latin, to_cyrillic

TOKEN = '5515635496:AAFWHxbv-pYBXN-nvwXXsz-kCgPp2nsua7U'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = 'Assalom Aleykum, Xush kelibsiz!'
    javob += '\nMatn kiriting '
    bot.reply_to(message, javob)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


if __name__ == "__main__":
    bot.polling()

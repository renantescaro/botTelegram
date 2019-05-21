import telebot
import re
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("813253543:AAFjGGHORTWYTe1l10w4nBBfCvzykhBbLu8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, u"Olá, bem-vindo ao bot!")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, u"Como posso te ajudar?")

@bot.message_handler(commands=['kanegae'])
def send_welcome(message):
    bot.reply_to(message, u"Oi Kanegae, tudo bem? :)")

def rotina(mensagem):
    print("teste 1")
    print("fazer algo aqui")
    print("digitou: " + mensagem)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if re.search('\\boi\\b', message.text, re.IGNORECASE):
	       bot.reply_to(message, "Olá, tudo bem?")

    if re.search('\\bbem\\b', message.text, re.IGNORECASE):
	       bot.reply_to(message, "Tudo ótimo!")

    if re.search('\\bnome\\b', message.text, re.IGNORECASE):
	       bot.reply_to(message, "Eu me chamo RaspDeath! :)")

    if re.search('\\bfala\\b', message.text, re.IGNORECASE):
	       bot.reply_to(message, "Falo sim! Quer conversar sobre o que?")

    if re.search('\\bteste\\b', message.text, re.IGNORECASE):
	       bot.reply_to(message, "Esta me testando?")

    if re.search('\\bw4x\\b', message.text, re.IGNORECASE):
        rotina(message.text)

bot.polling(none_stop=True)

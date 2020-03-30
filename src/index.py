import telebot
from dotenv import load_dotenv
import os

from messageHandlers.start import sendStart

load_dotenv()

botToken = os.getenv('BOTTOKEN')

bot = telebot.TeleBot(botToken)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)


bot.polling()

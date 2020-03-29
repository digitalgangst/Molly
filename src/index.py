import telebot
from dotenv import load_dotenv
import os

load_dotenv()

botToken = os.getenv('BOTTOKEN')

bot = telebot.TeleBot(botToken)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Howdy, how are you doing')


bot.polling()

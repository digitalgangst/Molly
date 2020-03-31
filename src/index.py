import os
import re
import telebot


from dotenv import load_dotenv
from commands.reply.sedCommand import SedCommand

from core.command import AuthCommand

load_dotenv()

botToken = os.getenv('BOTTOKEN')

bot = telebot.TeleBot(botToken)

replyCommands = [SedCommand]


@bot.message_handler(commands=['isalive'])
def send_welcome(message):
    bot.reply_to(message, 'Fuck Yeah!')

# Regex Replace
@bot.message_handler(func=lambda message: message.reply_to_message)
def replace_regex_msg(message):
    c = AuthCommand()
    for command in replyCommands:
        cmd = command()
        cmd.load(bot)
        cmd.exec(message)


bot.polling()

import os
import re
from commands.reply.sedCommand import SedCommand

import telebot

from core.command import AuthCommand
from core.credentials import getToken
from core.repository import Repository

botToken = getToken()

bot = telebot.TeleBot(botToken)

replyCommands = [SedCommand]

print(Repository.findAllAdmins())


@bot.message_handler(commands=['isalive'])
def send_welcome(message):
    bot.reply_to(message, 'Fuck Yeah!')

# Regex Replace
@bot.message_handler(func=lambda message: message.reply_to_message)
def replace_regex_msg(message):
    c = AuthCommand(Repository)
    for command in replyCommands:
        cmd = command()
        cmd.load(bot)
        cmd.exec(message)


bot.polling()

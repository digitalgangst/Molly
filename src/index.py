import telebot
from dotenv import load_dotenv
import os
import re

load_dotenv()

botToken = os.getenv('BOTTOKEN')

bot = telebot.TeleBot(botToken)


@bot.message_handler(commands=['isalive'])
def send_welcome(message):
    bot.reply_to(message, 'Fuck Yeah!')

# Regex Replace
@bot.message_handler(func=lambda message: message.reply_to_message)
def replace_regex_msg(message):
    data = re.search("s\/(.*?)\/(.*?)\/?$", message.text.strip())
    if not data: # valida a regex
        return
    message_foredit = message.reply_to_message # mensagem a ser editada
    msg_origin, msg_sub = data.group(1), data.group(2)
    try: # valida a regex do usuario
        msg = re.sub(msg_origin, msg_sub, message_foredit.text)
        bot.reply_to(message.reply_to_message, "*Você quis dizer:* \n \"{0}\" ".format(msg), parse_mode="Markdown")
    except re.error:
        bot.reply_to(message.reply_to_message, "*E:* regex error", parse_mode="Markdown")

bot.polling()

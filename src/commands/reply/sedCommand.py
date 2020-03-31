import re

from core.command import Command


class SedCommand(Command):

    def __init__(self):
        super().__init__()
        self.bot = None

    def load(self, bot):
        self.bot = bot

    def exec(self, message):
        bot = self.bot
        data = re.search("s\/(.*?)\/(.*?)\/?$", message.text.strip())
        if not data:
            return
        message_foredit = message.reply_to_message
        msg_origin, msg_sub = data.group(1), data.group(2)
        try:
            msg = re.sub(msg_origin, msg_sub, message_foredit.text)
            bot.reply_to(message.reply_to_message,
                         "*Você quis dizer:* \n \"{0}\" ".format(msg), parse_mode="Markdown")
        except re.error:
            bot.reply_to(message.reply_to_message,
                         "*E:* regex error", parse_mode="Markdown")

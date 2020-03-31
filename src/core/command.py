import re
import json

from core.repository import Repository

class Command:
    def __init__(self):
        super().__init__()
        self.bot = None

    def load(self, bot):
        self.bot = bot

    def exec(self, message):
        pass


class AuthCommand:
    def __init__(self, repository = Repository):
        super().__init__()
        self.authorizedIds = repository.findAllAdmins()
        self.bot = None

    def load(self, bot):
        self.bot = bot

    def command(self, message):
        pass

    def useCustomError(self):
        return False

    def onError(self, message):
        pass

    def exec(self, message):
        bot = self.bot
        id = message.from_user.id
        if id in self.authorizedIds:
            return self.command(message)
        if self.useCustomError():
            return self.onError(message)
        return bot.reply_to(message.reply_to_message, "Não autorizado")

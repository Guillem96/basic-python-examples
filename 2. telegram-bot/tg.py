import telegram
from telegram.ext import MessageFilter, Filters


class LambdaFilter(telegram.ext.UpdateFilter):

    def __init__(self, when):
        self.when = when

    def filter(self, message):
        return self.when(message.text)


class StartsWithFilter(telegram.ext.MessageFilter):
    def __init__(self, prefix):
        self.prefix = prefix

    def filter(self, message):
        return message.startswith(message.text)


class ContainsFilter(telegram.ext.MessageFilter):
    def __init__(self, content):
        self.content = content

    def filter(self, message):
        return self.content in message.text


class MatchesFilter(telegram.ext.MessageFilter):
    def __init__(self, target):
        self.target = target

    def filter(self, message):
        return self.target == message.text

ANY_MESSAGE = Filters.text & ~Filters.command
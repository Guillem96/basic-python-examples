import telegram
from telegram.ext import Filters, MessageFilter, MessageHandler


class _LambdaFilter(telegram.ext.UpdateFilter):
    def __init__(self, when):
        self.when = when

    def filter(self, message):
        return self.when(message.text)


class _StartsWithFilter(telegram.ext.MessageFilter):
    def __init__(self, prefix):
        self.prefix = prefix

    def filter(self, message):
        return message.startswith(message.text)


class _ContainsFilter(telegram.ext.MessageFilter):
    def __init__(self, content):
        self.content = content

    def filter(self, message):
        return self.content in message.text


class _MatchesFilter(telegram.ext.MessageFilter):
    def __init__(self, target):
        self.target = target

    def filter(self, message):
        return self.target == message.text


def CustomFunctionMatch(fn, cb):
    return MessageHandler(_LambdaFilter(fn), cb)


def StartsWith(target, cb):
    return MessageHandler(_StartsWithFilter(target), cb)


def Contains(target, cb):
    return MessageHandler(_ContainsFilter(target), cb)


def MessageMatches(target, cb):
    return MessageHandler(_MatchesFilter(target), cb)


def AnyMessage(cb):
    return MessageHandler(Filters.text, cb)


################################################################################


def send_photo(message, photo_path):
    if photo_path.startswith('http'):
        message.reply_photo(photo_path)
    else:
        message.reply_photo(open(photo_path, 'rb'))

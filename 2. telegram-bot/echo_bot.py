import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
    # Here we receive an update object (https://python-telegram-bot.readthedocs.io/en/stable/telegram.update.html?highlight=Update#telegram-update)
    # Update object contains a message object
    message = update.message
    # With Message we can reply with text, images, audio, etc..
    # https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html
    message.reply_text('Hi!')


def echo(update, context):
    update.message.reply_text(update.message.text)


def main():

    updater = Updater(os.environ["TOKEN"], use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

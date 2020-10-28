from telegram.ext import Updater, CommandHandler, MessageHandler
from tg import *


def send_dog(update, context):
    message = update.message
    message.reply_text('dog')
    send_photo(message, 'images/dog.jpg')


def send_cat(update, context):
    message = update.message
    send_photo(message, 'images/cat.jpg')



def main():
    updater = Updater("1320980940:AAF9x4QamW8bnCmMyQz8U6f-w1nGjCOjrhY", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(MatchesFilter("dog"), send_dog))
    dp.add_handler(MessageHandler(MatchesFilter("cat"), send_cat))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

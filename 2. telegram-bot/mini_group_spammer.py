
import os
import requests

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


################################################################################

groups = dict()


################################################################################

def start(update, context):
    """Send a message when the command /start is issued."""

    update.message.reply_markdown("""
    Hi! I am a SPAM message replicator to groups
    """)


def help_command(update, context):
    update.message.reply_text('You have two commands:\n- /savegroup ALIAS\n'
                              '- /sendtogroup ALIAS MESSAGE')


def save_group_callback(update, context):
    msgtokens = update.message.text.split(" ")
    groupchatid = update.message.chat_id
    groups[msgtokens[1]] = groupchatid
    update.message.reply_text("Getting group ID" + str(groupchatid) + " as " + msgtokens[1])


def send_message_group(update, context):
   msgtokens = update.message.text.split(" ")
   group = msgtokens[1]
   message = " ".join(msgtokens[2:])
   context.bot.send_message(chat_id=groups[msgtokens[1]], text=message)


################################################################################

def main():

    updater = Updater("TOKEN", 
                      use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("savegroup", save_group_callback))
    dp.add_handler(CommandHandler("sendtogroup", send_message_group))

    updater.start_polling()

    print('Running bot...')
    updater.idle()


if __name__ == "__main__":
    main()

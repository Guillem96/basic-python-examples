from telegram.ext import Updater, CommandHandler, MessageHandler
from tg import *

def callback(update, ctx):
    message = update.message
    # TODO: Your callback code
  
def main():
    updater = Updater("TOKEN", use_context=True)
    dp = updater.dispatcher

    # TODO: Setup your bot here
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

import time

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler


class Notifier:

    def __init__(self, token, data_file):

        self.token = token
        self.data_file = data_file
        self.previous_lines = 0

        self.subscribed = []
        self.updater = Updater(self.token, use_context=True)

    def help_callback(self, update, context):
        text = """
        Available commands:
        - /help: Ask for help
        - /subscribe: Subscribe to crypto currencies notifications
        - /unsubscribe: Revoke subscription
        """
        update.message.reply_text(text)

    def start_callback(self, update, context):
        text = """
        Hello!

        I am a bot that notifies you every minute about the new crypto currency
        rates.

        If you want to subscribe to my notifications type /subscribe
        """
        update.message.reply_text(text)

    def subscribe_callback(self, update, context):
        chat_id = update.message.chat_id
        self.subscribed.append(chat_id)
        update.message.reply_text("Subscription completed successfully ✅")

    def unsubscribe_callback(self, update, context):
        chat_id = update.message.chat_id
        if chat_id not in self.subscribed:
            update.message.reply_text("You cannot revoke the subscription since "
                                      "you are not subscribed ❌")
        else:
            self.subscribed.remove(chat_id)
            update.message.reply_text("Subscription removed 👌")

    def configure_bot(self):

        dp = self.updater.dispatcher

        # Displays a small description about the bot
        dp.add_handler(CommandHandler("start", self.start_callback))

        # Ask for help, basically to know which commands are available
        dp.add_handler(CommandHandler("help", self.help_callback))

        dp.add_handler(CommandHandler("subscribe", self.subscribe_callback))
        dp.add_handler(CommandHandler("unsubscribe", self.unsubscribe_callback))

    def send_notification(self):
        f = open(self.data_file)
        lines = f.readlines()

        if len(lines) != self.previous_lines:
            # Send the notification
            data = lines[-1]
            data = data.split(',')

            message = (f"1 Bitcoin is equal to {data[0]}€\n"
                       f"1 Cardano is equal to {data[1]}€\n"
                       f"1 Ethereum is equal to {data[2]}€\n"
                       f"1 IOTA is equal to {data[3]}€\n"
                       f"1 Tether is equal to {data[4]}€")

            for subscriber in self.subscribed:
                self.updater.bot.send_message(subscriber, message)

            self.previous_lines = len(lines)

        f.close()

    def start_bot(self):
        print('Running bot...')
        self.updater.start_polling()
        while True:
            time.sleep(10)
            self.send_notification()


def main():
    notifier = Notifier("1320980940:AAF9x4QamW8bnCmMyQz8U6f-w1nGjCOjrhY", 
                        'cryptos.csv')
    notifier.configure_bot()
    notifier.start_bot()


if __name__ == "__main__":
    main()

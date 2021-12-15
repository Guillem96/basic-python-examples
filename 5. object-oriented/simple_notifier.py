from telegram.ext import Updater, CommandHandler


class Notifier:

    def __init__(self, token):
        self.token = token
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
        if chat_id not in self.subscribed:
            self.subscribed.append(chat_id)
            update.message.reply_text("Subscription completed successfully ✅")
        else:
            update.message.reply_text("You are already subscribed ❌")

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

    def send_notification(self, message):
        """Sends messages to the subscribed users.
        """
        for subscriber in self.subscribed:
            print(f"Sending message '{message}' to {subscriber}...")
            self.updater.bot.send_message(subscriber, message)

    def start(self):
        self.updater.start_polling()
        while True:
            txt = input("Text to notify: ")
            if txt:
                self.send_notification(txt)


if __name__ == "__main__":
    bot = Notifier("TOKEN")
    bot.configure_bot()
    bot.start()

import random
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler


player = {
    # TODO: Copy your player dict here
}

shop = {
    # TODO: Copy your mart dict here
}


def list_shop_items(update, context):
    """
    Generate a string containing all the available shop items along with
    its price and stock.
    Reply the message with the generated string

    Examples
    --------
    >>> my_string_list = "..."
    >>> message = update.message
    >>> message.reply_text(my_string_list)
    """
    pass


def player_inventory(update, context):
    """
    Same as `list_shop_items` but with player inventory
    """
    pass


def buy_callback(update, context):
    """
    Implement here the buy logic developed in the previous exercise.
    Reply to the user with an error message if he cannot complete the trade.
    If the trade is successfully completed answer the command with a success 
    message.

    Notes
    ----
    The message contains both, the command (/buy) and the `item_name`

    >>> message_text = update.message.text # '/buy sword'
    >>> item_name = message_text[5:] # We skip the command and the whitespace
    """
    pass


def sell_callback(update, context):
    """
    Same as `buy_callback`, but this time selling

    Notes
    -----
    Again, the text message is composed of the command + the item_name
    """
    pass


def help_command(update, context):
    text = """
    Available commands:

    - */help*: Ask for help
    - */inventory*: List player's status (items and gold)
    - */shopitems*: List available shop items
    - */buy*: Buy an item. Expects an item name by parameter
    """
    update.message.reply_text(text, parse_mode=telegram.ParseMode.MARKDOWN)


def main():
    updater = Updater("TOKEN", use_context=True)
    dp = updater.dispatcher

    # Ask for help, basically to know which commands are available
    dp.add_handler(CommandHandler("help", help_command))

    # List the player inventory, including the gold
    dp.add_handler(CommandHandler("inventory", player_inventory))

    # Buys an item. To invoke this command you have to provide an extra argument
    # Example: /buy sword
    dp.add_handler(CommandHandler("buy", buy_callback))

    # Sells an item. To invoke this command you have to provide an extra argument
    # Example: /sell apple
    dp.add_handler(CommandHandler("sell", sell_callback))

    # List the available shop items
    dp.add_handler(CommandHandler("shopitems", list_shop_items))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

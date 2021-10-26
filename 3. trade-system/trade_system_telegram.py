import os
import random

from telegram.ext import CommandHandler, Updater

from tg import AnyMessage

player = {"gold": 21, "inventory": {"sword": 1, "apple": 3}}

shop = {
    "stock": {
        "shield": 3,
        "special sword": 2,
        "apple": 10,
        "wood log": 99,
    },
    "prices": {
        "shield": 100,
        "special sword": 500,
        "apple": 2,
        "wood log": 1,
    }
}


def shop_info_cb(update, context):
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
    result = "Shop\n----\n* Stocks\n"
    for item, stock in shop["stock"].items():
        result += item + " x" + str(stock) + "\n"

    result += "\n* Prices\n"
    for item, price in shop["prices"].items():
        result += item + f" {price}$\n"

    update.message.reply_text(result)


def player_info_cb(update, context):
    """
    Same as `list_shop_items` but with player inventory
    """
    result = "* Gold: " + str(player["gold"]) + "\n"

    result += "* Inventory\n"
    for item, qty in player["inventory"].items():
        result += item + " x" + str(qty) + "\n"

    update.message.reply_text(result)


def buy(player, shop, item_name):
    if item_name not in shop:
        return False
    elif player["gold"] < shop["prices"][item_name]:
        return False
    elif shop["stock"][item_name] <= 0:
        return False
    else:
        player["gold"] -= shop["prices"][item_name]

        if item_name in player["inventory"]:
            player["inventory"][item_name] += 1
        else:
            player["inventory"][item_name] = 1

        shop["stock"][item_name] -= 1

        return True


def buy_cb(update, context):
    """
    Implement here the buy logic developed in the previous exercise.
    Reply to the user with an error message if he cannot complete the trade.
    If the trade is successfully completed answer the command with a success 
    message.

    Notes
    ----
    The message contains both, the command (/buy) and the `item_name`
    >>> message_text = update.message.text # "/sell sword"
    >>> item_name = message_text[5:] # We skip the command and the whitespace
    """
    message_text = update.message.text  # /buy sword
    if message_text == "/buy":
        update.message.reply_text("Missing item name")
    else:
        item_name = message_text[5:]  # sword
        if buy(player, shop, item_name):
            update.message.reply_text("You successfully bought " + item_name)
        else:
            update.message.reply_text("You cannot buy " + item_name)


def sell(player, shop, item_name):
    if player['inventory'][item_name] <= 0 or item_name not in shop['prices']:
        return False
    else:
        player['gold'] += shop['prices'][item_name] // 2
        player['inventory'][item_name] -= 1
        shop['stock'][item_name] += 1
        if player['inventory'][item_name] == 0:
            del player['inventory'][item_name]

        return True


def sell_cb(update, context):
    """
    Same as `buy_callback`, but this time selling
    Notes
    -----
    Again, the text message is composed of the command + the item_name
    """
    message_text = update.message.text  # /sell sword
    if message_text == "/buy":
        update.message.reply_text("Missing item name")
    else:
        item_name = message_text[6:]  # sword
        if sell(player, shop, item_name):
            update.message.reply_text("You successfully sold " + item_name)
        else:
            update.message.reply_text("You cannot sell " + item_name)


def help_command_cb(update, context):
    text = """
    Available commands:
    - /help: Ask for help
    - /playerinfo: List player"s status (items and gold)
    - /shopinfo: List available shop items
    - /buy: Buy an item. Expects an item name by parameter
    """
    update.message.reply_text(text)


def any_message_cb(update, context):
    update.message.reply_text(f"Invalid text: '{update.message.text}'")
    help_command_cb(update, context)


def main():
    updater = Updater(os.environ["TOKEN"], use_context=True)
    dp = updater.dispatcher

    # Ask for help, basically to know which commands are available
    dp.add_handler(CommandHandler("help", help_command_cb))

    # List the player inventory, including the gold
    dp.add_handler(CommandHandler("playerinfo", player_info_cb))

    # Buys an item. To invoke this command you have to provide an extra argument
    # Example: /buy sword
    dp.add_handler(CommandHandler("buy", buy_cb))

    # Sells an item. To invoke this command you have to provide an extra argument
    # Example: /sell apple
    dp.add_handler(CommandHandler("sell", sell_cb))

    # List the available shop items
    dp.add_handler(CommandHandler("shopinfo", shop_info_cb))

    # Reply to any other message
    dp.add_handler(AnyMessage(any_message_cb))

    print("Running bot...")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

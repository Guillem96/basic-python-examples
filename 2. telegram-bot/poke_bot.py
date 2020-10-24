"""
Bot ID: pokebot
Bot Username: ProgrammingPokeBot
Profile URL: t.me/ProgrammingPokeBot
"""

import os
import requests

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


################################################################################

def find_by_name(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    response = requests.get(url)
    if response.status_code > 300:
        return None
    else:
        return response.json()


################################################################################

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_markdown("""
    Hi! I am a **Pokemon Bot**

    Send me a pokemon name and I'll respond you with his sprite. And some
    intersting facts about him.
    """)


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('You have to send me a pokemon name')


def pokemon(update, context):
    pokemon_name = update.message.text
    pokemon = find_by_name(pokemon_name.lower())
    if pokemon is None:
        update.message.reply_text(f'Pokemon "{pokemon_name}" does not exist...')
        return

    sprite_url = pokemon['sprites']['other']['official-artwork']['front_default']
    update.message.reply_photo(sprite_url)

    metadata = f"Pokemon ID: {pokemon['id']}\n"
    stats = '\n'.join(f"*{o['stat']['name'].capitalize()}*: {o['base_stat']}" 
                      for o in pokemon['stats'])
    message = f"*Pokemon data* \n{metadata}*Stats* \n{stats}"
    update.message.reply_text(message, parse_mode=telegram.ParseMode.MARKDOWN)


################################################################################

def main():

    updater = Updater(os.environ['TOKEN'], use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, pokemon))

    updater.start_polling()

    print('Running bot...')
    updater.idle()


if __name__ == "__main__":
    main()
"""
Bot ID: pokebot
Bot Username: ProgrammingPokeBot
Profile URL: t.me/ProgrammingPokeBot
"""

import os
import random
import requests

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import tg


################################################################################

def find_by_name(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    response = requests.get(url)
    if response.status_code > 300:
        return None
    else:
        return response.json()


################################################################################

def start(update, context):
    """Send a message when the command /start is issued."""

    update.message.reply_text("""
Hi! I am a *Pokemon Bot*
Send me a pokemon name and I'll respond you with his sprite. And some intersting facts about him.
    """, parse_mode=telegram.ParseMode.MARKDOWN)


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
    send_photo(message, sprite_url)
    update.message.reply_text(_fmt_pkmn_stats(pokemon),
                              parse_mode=telegram.ParseMode.MARKDOWN)


def rand_pokemon(update, context):
    pokemon_name = update.message.text
    pokemon = find_by_name(str(random.randint(0, 152)))
    if pokemon is None:
        update.message.reply_text(f'Pokemon "{pokemon_name}" does not exist...')
        return

    sprite_url = pokemon['sprites']['other']['official-artwork']['front_default']
    update.message.reply_photo(sprite_url)
    update.message.reply_text(_fmt_pkmn_stats(pokemon),
                              parse_mode=telegram.ParseMode.MARKDOWN)


def _fmt_pkmn_stats(pokemon):
    metadata = f"Pokemon ID: {pokemon['id']}\n"
    metadata += f"Name: {pokemon['name'].capitalize()}"
    stats = '\n'.join(f"*{o['stat']['name'].capitalize()}*: {o['base_stat']}" 
                      for o in pokemon['stats'])
    return f"*Pokemon data* \n{metadata} \n*Stats* \n{stats}"


################################################################################

def main():
    updater = Updater(os.environ['TOKEN'], use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    random_pkm_filter = tg.MatchesFilter('!random')

    dp.add_handler(MessageHandler(random_pkm_filter & ~Filters.command, rand_pokemon))
    dp.add_handler(MessageHandler(Filters.text & 
                                  ~Filters.command & 
                                  ~random_pkm_filter, pokemon))
    updater.start_polling()

    print('Running bot...')
    updater.idle()


if __name__ == "__main__":
    main()
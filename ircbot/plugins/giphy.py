import random
import requests

from ircbot import bot

giphy_url = "https://api.giphy.com/v1/gifs/search"
giphy_api = bot.config['Giphy']['api_key']


@bot.command('giphy')
def giphy(bot, channel, sender, args):
    """Usage: {bot.trigger}giphy [tag] - Finds a random gif, or returns a random gif tagged with [tag]"""

    params = (('api_key', giphy_api), ('q', " ".join(args)), ('limit', '25'))
    resp = requests.get(giphy_url, params=params).json()

    gif_url = resp['data'][random.randint(1, 25)]['images']['original']['webp']

    bot.message(channel, gif_url)

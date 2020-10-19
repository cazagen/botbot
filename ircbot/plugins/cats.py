import requests

from ircbot import bot


@bot.command('cat')
def cat_command(bot, channel, sender, args):
    """Usage: {bot.trigger}cat - Posts a cat gif!"""
    uri = "https://aws.random.cat/meow"
    data = requests.get(uri).json()
    bot.message(channel, "{}".format(data['file']))

import requests

from ircbot import bot


def get_asn_owner(asn):
    endpoint = "https://api.bgpview.io/asn/{}".format(asn)

    resp = requests.get(endpoint)

    return resp.json()['data']['description_short']


@bot.command('asn')
def command(bot, channel, sender, args):
    """Lookup the owner of an AS number. Usage: {bot.trigger}asn 1234"""
    if len(args) < 1:
        bot.message(channel, "This command requires an argument, e.g. {}asn 1234".format(bot.trigger))
        return

    owner = get_asn_owner(args[0])

    bot.message(channel, "{}: The owner of AS{} is {}".format(sender, args[0], owner))

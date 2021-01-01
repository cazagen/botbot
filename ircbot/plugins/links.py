import requests
import requests.exceptions
import re
from bs4 import BeautifulSoup
from ircbot import bot

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def allowed_to_process(bot, channel):
    mode = bot.config['Links']['mode']

    if mode == "all":
        return True

    if mode == "whitelist" and channel in bot.config['Links']['channels']:
        return True
    elif mode == "whitelist":
        return False

    if mode == "blacklist" and channel in bot.config['Links']['channels']:
        return False

    return True


def truncate_title(title):
    title = title.replace("\n", "")
    max_length = int(bot.config['Links']['max_length'])
    if len(title) > max_length:
        return "{}...".format(title[:max_length])
    else:
        return title


@bot.hook()
def link_title_parse_hook(bot, channel, sender, message):
    if not allowed_to_process(bot, channel):
        return

    for word in message.split(" "):
        try:
            if re.match(regex, word):
                r = requests.get(word)

                if r.status_code != 200:
                    return

                soup = BeautifulSoup(r.text, 'html.parser')
                title = soup.head.title.text.strip()
                title = truncate_title(title)

                if title:
                    bot.message(channel, "🔗 {}".format(title))
        except requests.exceptions.InvalidSchema:
            pass

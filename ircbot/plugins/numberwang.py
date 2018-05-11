import random

from ircbot import bot

wang_counter = 0
wang_level = random.randint(4, 10)
wang_ratio = 0.4


@bot.hook()
def message_hook(bot, channel, sender, message):
    global wang_counter

    number_count = 0
    message_length = len(message)

    for char in message:
        if char.isdigit():
            number_count = number_count + 1

    if number_count / message_length >= wang_ratio:
        wang_counter = wang_counter + 1

    if wang_counter == wang_level:
        wang_counter = 0
        bot.message(channel, "NUMBERWANG")

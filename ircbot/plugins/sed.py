from ircbot import bot

last_message = " "


@bot.hook()
def sed_handler(bot, channel, sender, message):
    global last_message
    if "s/" in message:
        sed = message.split("/")
        print(sed)
        bot.message(channel, "<{}> {}".format(sender, last_message.replace(sed[1], sed[2])))
    last_message = message

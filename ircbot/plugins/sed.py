from ircbot import bot

bot.last_message = " "


@bot.hook()
def sed_handler(bot, channel, sender, message):
    if "s/" in message:
        sed = message.split("/")
        print(sed)
        bot.message(channel, "<{}> {}".format(sender, bot.last_message.replace(sed[1], sed[2])))
    bot.last_message = message

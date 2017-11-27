import urbandictionary
import re

from ircbot import bot


@bot.command('ud')
def ud(bot, channel, sender, args):
    """ Defines you a word """
    definition = urbandictionary.define(" ".join(args))[0]
    bot.message(channel, "{}: {}".format(
        definition.word,
        definition.definition
    ))


@bot.command('udrandom')
def udrandom(bot, channel, sender, args):
    """ Defines you a random word from urban dictonary"""
    definition = urbandictionary.random()
    strip_empty(definition[0].definition)
    bot.message(channel, "{}: {}".format(
        definition[0].word,
        definition[0].definition
    ))

def strip_empty(definition):
    print(definition)
    new_definition = re.sub(r'\s{2}', ' ', definition)
    print(new_definition)
import json
import requests

from ircbot import bot

@bot.command('code')
def code(bot, channel, sender, args):
    """ Runs the given code (for code_id try {bot.trigger}listlanguages). ie: {bot.trigger}code [the actual code] [code_id]"""
    if args[-1] != "43":
        url = "https://api.judge0.com/submissions/"
        
        params = {
            "base64_encoded": "false",
            "wait": "true"
            }
        
        payload = {
            'source_code': str(" ".join(args[:-1])),
            'language_id': str(args[-1])}
        
        headers = {
            'content-type': "application/json"
            }
        
        print(payload)
    
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers, params=params)
        
        print(response.text)
        
        if "++" in response.json()['stdout']:
            bot.message(channel, "Don't be a butt")
            return
        
        if "--" in response.json()['stdout']:
            bot.message(channel, "Don't be a butt")
            return
        
        bot.message(channel, str(response.json()['stdout']))

@bot.command('listlanguages')
def languageChecker(bot, channel, sender, args):
    url = "https://api.judge0.com/languages"

    response = requests.get(url).json()

    languages = ""

    for entry in response:
        if entry['id'] == 43:
            continue
        else:
            languages += "{}: {} ".format(entry['id'], entry['name'])

    bot.message(channel, "The current languages I speak are: {}".format(languages))

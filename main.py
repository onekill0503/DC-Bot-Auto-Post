from __future__ import print_function
import discord
import random
import time
import numpy as np
import json
import chalk

# Load Configuration File
with open('./conf.json') as f:
  config = json.load(f)

# Open Default Wordlist
with open(config["default_wordlist"]) as w:
  wl = json.load(w)

class MyClient(discord.Client):
    async def on_ready(self):
      print('Logged on as {0}!'.format(self.user))
      
      # Define lastword
      last_word = {}
      for l in config["channel"] :
        last_word[l["channel_name"]] = ""
      
      # Running the Bot
      while (True):
        # Get Delay timer by range min_timer - max_timer (min_timer + 2 minutes)
        delay = random.randrange(config["min_timer"], (config["min_timer"] + (60*1.5) ))

        # Getting channel data
        channel_data = np.random.choice(config["channel"],size=1)
        chan = self.get_channel(channel_data[0]["channel_id"])
        
        # Generate Word
        try :
            ca = channel_data[0]["custom_wordlist"]
        except KeyError:
            ca = ""
        if ca :
          try :
            with open(config["custom_wordlist"][channel_data[0]["custom_wordlist"]]) as cw:
              custom_word = json.load(cw)
          except FileNotFoundError:
            print(chalk.yellow("[WARNING] ") + "Can't Find Custom Wordlist file at \n" + config["custom_wordlist"][channel_data[0]["custom_wordlist"]])
            print(chalk.yellow("[WARNING] ") + "Using Default Wordlist !")
            custom_word = wl
            
          word = np.random.choice(custom_word,size=1)[0]
        else :
          word = np.random.choice(wl, size=1)[0]

        if last_word[channel_data[0]["channel_name"]] != word :
          # Sent Message
          try:      
            await chan.send(word)
            last_word[channel_data[0]["channel_name"]] = word
            print(chalk.green("[SUCCESS] ") + "Sent ["+ chalk.green('word') +"] at " + channel_data[0]["channel_name"] + "...")
          except discord.errors.Forbidden:
            print(chalk.red("[ERROR] ") + "You have not access to the channel (Timedout / On Cooldown)")
          except:
            print(chalk.red("[ERROR] ") + "Unknow Error")
          # Create Delay
          print(chalk.yellow("Waiting "+ str(delay) +" secs..."))
          try:
            time.sleep(delay)
          except KeyboardInterrupt:
            print(chalk.yellow("[WARNING] " + "Program Exited !"))

client = MyClient()
client.run(config["account_token"], bot=False)

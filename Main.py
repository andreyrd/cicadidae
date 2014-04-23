import json

from tk.jomp16.cicadidae.irc.IrcManager import IrcManager


__author__ = 'jomp16'

config = json.load(open("config.json", "r"))

ircManager = IrcManager(config)

ircManager.connect()

# for server in config["servers"]:
#    print(config["servers"][server])
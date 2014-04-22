import bot
import json

ConfigFile = open( "config.json", "r+" )

print("Loading config file...")

Config = json.load( ConfigFile )  

print("Decoding config file into python object...")

ConfigFile.close()

ThreadList = []
for Server in Config["servers"]:
    ThreadList.append(bot.ServerThreads( Config, Config["servers"][Server], Config["channels"][Server] ))
    (max(ThreadList)).start()
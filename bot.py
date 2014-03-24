import sys
import irc.client

prefix = "@"

def on_connect(connection, event):
    connection.join("#amagital")

def on_pub_msg(connection, event):
    if event.arguments[0][0:1] == prefix :
        on_command(connection, event.target, event.arguments[0][1:])

def on_command(connection, target, command):
    if command[0:5] == "echo " :
        connection.privmsg(target, command[5:])

client = irc.client.IRC()
try: 
    con = client.server().connect("irc.freenode.net", 6667, "bestbotever")
except irc.client.ServerConnectionError:
    print(sys.exc_info()[1])
    sys.exit(1)
con.add_global_handler("welcome", on_connect)
con.add_global_handler("pubmsg", on_pub_msg)

client.process_forever()
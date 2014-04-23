import re
import socket
import threading

from tk.jomp16.cicadidae.irc.output.OutputIrc import OutputIrc
from tk.jomp16.cicadidae.irc.output.OutputRaw import OutputRaw


__author__ = 'jomp16'


class IrcManager:
    outputRaw = None
    outputIrc = None
    socket1 = None
    thread = None

    def __init__(self, config):
        self.config = config

    def connect(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        self.socket1 = socket.socket()
        self.socket1.connect((self.config["server"]["address"], self.config["server"]["port"]))
        self.outputRaw = OutputRaw(self.socket1)
        self.outputIrc = OutputIrc(self)

        self.outputRaw.sendMessage("NICK " + self.config["server"]["identity"]["name"])
        self.outputRaw.sendMessage(
            "USER " + self.config["server"]["identity"]["ident"] + " 8 * " + self.config["server"]["identity"][
                "realname"])

        socketAsFile = self.socket1.makefile()

        self.outputIrc.joinChannel("##waratte")

        while True:
            line = socketAsFile.readline()

            if not line:
                break

            print(line)

            # todo: change this to event driven
            matchedObject = re.match(r'^PING (.*?)$', line)
            if matchedObject:
                self.outputRaw.sendMessage("PONG: " + matchedObject.group)
__author__ = 'jomp16'


class OutputRaw:
    def __init__(self, socket):
        self.socket = socket

    def sendMessage(self, message):
        print("[BOT]: " + message)
        self.socket.send((message + "\r\n").encode())
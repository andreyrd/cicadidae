__author__ = 'jomp16'


class OutputIrc:
    def __init__(self, ircManager):
        self.ircManager = ircManager

    def joinChannel(self, channel):
        self.ircManager.outputRaw.sendMessage("JOIN :" + channel)

    def partChannel(self, channel):
        self.ircManager.outputRaw.sendMessage("PART :" + channel)
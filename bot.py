import sys 
import socket
import threading
import time
import re

def socketSend( Socket, String ):
    "coverts a string to send to a socket"
    
    Socket.send( String.encode() )
    
class ServerThreads (threading.Thread):
    def __init__(self, Config, Server, Channels):
        threading.Thread.__init__(self)
        self.Config = Config
        self.Server = Server
        self.Channels = Channels
        
    def run(self):
        "template for IRC server loop"
    
        Socket = socket.socket()
        
        print("Connecting to %s at port %i..." % (self.Server["address"], self.Server["port"]) )
        Socket.connect((self.Server["address"], self.Server["port"]))
        SocketAsFile = Socket.makefile()
            
        while True:
            Line = SocketAsFile.readline()
            if Line.find("376"):
                break
                
            else:
                print( '[%s] %s' % (self.Server["name"], Line) )

        socketSend(Socket, 'NICK %s\r\n' % self.Server["identity"]["name"])
        print( "[BOT] " + "NICK %s" % self.Server["identity"]["name"] )
        
        socketSend(Socket, 'USER %s %s bla :%s\r\n' % (self.Server["identity"]["ident"], 
                                                       self.Server["identity"]["hostname"], 
                                                       self.Server["identity"]["realname"]))
                                                  
        print("[BOT] " + "USER %s %s bla :%s" % (self.Server["identity"]["ident"], 
                                                   self.Server["identity"]["hostname"], 
                                                   self.Server["identity"]["realname"]))

        for Channel in self.Channels:
            socketSend(Socket, 'JOIN :%s\r\n' % Channel["name"])
            print("[BOT] " + "JOIN :%s" % Channel["name"])
            
            socketSend(Socket, 'PRIVMSG %s :%s\r\n' % (Channel["name"], "I got 99 problems but connecting to IRC ain't one."))
            print("[BOT] " + "PRIVMSG %s :%s" % (Channel["name"], "I got 99 problems but connecting to IRC ain't one."))

        while True: #Max size of an IRC message (512) * the amount of bytes in a unicode string (4)
            time.sleep(0.1)
        
            Line = SocketAsFile.readline()
            
            if not Line:
                break
            
            MatchedObject = re.match(r'^PING (.*?)$', Line)
            if MatchedObject:
                socketSend(Socket, 'PONG %s\r\n' % MatchedObject.group())
                print("[BOT] " + "PONG %s" % MatchedObject.group())
            
            MatchedObject2 = re.search(r'die', Line)
            if MatchedObject2:
                socketSend(Socket, 'QUIT :Fine, meanie >:(\r\n')
                print("[BOT] " + "QUIT :Fine, meanie >:(")
                break;
                
            else:
                print( '[%s] %s' % (self.Server["name"], Line) )
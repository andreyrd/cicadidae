import sqlite3

def socketSend( Socket, String ):
    "coverts a string to send to a socket"
    
    Socket.send( String.encode() )
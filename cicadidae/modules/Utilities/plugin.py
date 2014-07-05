from data.include import socketSend

def die( reason ):
    
    socketSend(Socket, 'QUIT :' + reason + '\r\n')
    print("[BOT] " + "QUIT :" + reason)